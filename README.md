# secretsdump-parser
When you dump hashes via Impacket-secretsdump, you can crack the dumped hashes.
After the cracking process how do you know which password corresponds to which user in your dump? Here comes **secretdump-parser**! 
It takes in input 3 file:

  * secretsdump: the dump file
  * crackedhashes: a file containing the cracked hashes and the plaintext version in format **hash:cleartext_pwd**
  * outfile: the path for the outputfile

The parser will create a file in the format **username:cleartext_pwd**

## Example ##

Let's say you have dumped some hashes and in your dump file there is:

  * Administrator:12131:aad3b435b51404eeaad3b435b51404ee:8846F7EAEE8FB117AD06BDD830B7586C:::


After cracking the hash you discover the password is:

  * password
  
  
You need a file containing:

  * 8846F7EAEE8FB117AD06BDD830B7586C:password
  
That's all you need! Run the parser and you will end up with the output file containing:
 
  * Administrator:password
