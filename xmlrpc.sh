#!/bin/bash

# Text design indicating XML-RPC
echo "=========================================="
echo "          XML-RPC Vulnerability Check      "
echo "=========================================="
echo "            developer by @MINADO          "
echo


# Menu function
menu() {
   echo "Choose an option:"
   echo "1. Check XML-RPC Endpoint"
   echo "2. Use ffuf to Fuzz All Directories"
   echo "3. Exit"
   read -p "Enter your choice: " choice

   case "$choice" in
      1)
         read -p "Enter the URL to check for XML-RPC vulnerability: " xmlrpc_url
         check_xml_rpc "$xmlrpc_url"
         ;;
      2)
         read -p "Enter the URL to fuzz directories: " fuzz_url
         read -p "Enter the path to your wordlist: " wordlist_path
         use_ffuf "$fuzz_url" "$wordlist_path"
         ;;
      3)
         exit 0
         ;;
      *)
         echo "Invalid choice. Please select a valid option."
         menu
         ;;
   esac
}

check_xml_rpc() {
   # Check for the required argument
   if [ "$#" -ne 1 ]; then
      echo "Usage: $0 <URL>"
      exit 1
   fi

   # Define the URL
   local url="$1"

   # Define the directory you want to check
   directory_to_check="xmlrpc.php"

   # Create the full URL by appending the directory
   full_url="$url/$directory_to_check"

   # Array of XML-RPC methods to check for
   xml_rpc_methods=("wp.deleteCategory" "wp.suggestCategories" "wp.uploadFile")

   # Send a POST request with an XML-RPC payload
   xml_payload='<?xml version="1.0"?>
   <methodCall>
      <methodName>system.listMethods</methodName>
      <params></params>
   </methodCall>'

   # Send the POST request and capture both the response body and HTTP status code
   check=$(curl -s "$full_url")
   response=$(curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: text/xml" -d "$xml_payload" "$full_url")
   response_body=$(curl -s -X POST -H "Content-Type: text/xml" -d "$xml_payload" "$full_url")

   # Check if the HTTP status code is 200 and if the response body contains any of the XML-RPC methods
   is_vulnerable=false

   for method in "${xml_rpc_methods[@]}"; do
      if [ "$response" -eq 200 ] && echo "$response_body" | grep -iq "$method"; then
         is_vulnerable=true
         break
      fi
   done

   if [ "$is_vulnerable" = true ]; then
      echo "Vulnerable URL: $full_url"
      echo "Response:" $response
      if echo "$check" | grep -q "XML-RPC server accepts POST requests only";then
         echo "page result : XML-RPC server accepts POST requests only"
      fi
   else
      echo "Not vulnerable: $full_url"
   fi
}

use_ffuf() {

   # Check for the required arguments
   if [ "$#" -ne 2 ]; then
      echo "Usage: $0 <URL> <WORDLIST_PATH>"
      exit 1
   fi

   # Define the URL and wordlist from command line arguments
   local url="$1"
   local wordlist="$2"

   # Define the directory you want to check
   directory_to_check="xmlrpc.php"

   # Run ffuf with the specified options and store the output
   ffuf_output=$(ffuf -fc "404,403" -u "$url/FUZZ" -w "$wordlist" -o "xmlrpcFuzz.json")
   # Check if the directory exists in the ffuf output
   if echo "$ffuf_output" | grep -q "$directory_to_check"; then
      echo "Found: $url/$directory_to_check"

   else
      echo "Not found: $url/$directory_to_check"
   fi
}

menu