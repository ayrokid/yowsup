1. download : https://github.com/ayrokid/yowsup
2. wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python
3. sudo apt-get install python-pip
4. sudo pip install requests-oauth
5. sudo python setup.py install
6. sudo apt-get install python-mysqldb or # pip install mysql-python

7. # cp config.example yowsup-cli.config
   # cat yowsup-cli.config

8. # chmod +x yowsup-cli
   # ./yowsup-cli registration --requestcode sms --config yowsup-cli.config
   You should receive this on your terminal :
   status: sent
   retry_after: 3605
   length: 6
   method: sms
9. Registering the Code
   You will receive a message with the registration code and it will be in this format XXX-XXX
   # ./yowsup-cli registration --register XXX-XXX --config yowsup-cli.config

   Immedaitely, you will receive something on your terminal close to what is below here :
   status: ok
   kind: free
   pw: Q2nBGCvZhb7TBQrcm2sQCfSLgXM=     -----> Finally here is your password
   price: 0,89
   price_expiration: 1362803446
   currency: EUR
   cost: 0.89
   expiration: 1391344106
   login: 34123456789
   type: new

10. There you have it now you have a WhatsApp password
    So go back to your yowsup.config file and put in the new password
    # cat yowsup-cli.config
    cc=254 
    phone=254123456789 
    id=
    password= Q2nBGCvZhb7TBQrcm2sQCfSLgXM=

7. run apps : ./yowsup-cli demos --yowsup --login 6281390688955:Ga3lQvVTvzt10PlCGC/W5MAJfuE=


reverensi : http://kennethkinyanjui.info/whatsapp-on-laptop.html

note : 
jika python setup.py install error coba install :
pip install https://pypi.python.org/packages/source/p/python-axolotl/python-axolotl-0.1.7.tar.gz




