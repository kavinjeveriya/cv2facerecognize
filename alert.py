

def mail():
    import smtplib
    sender_email = "swapnilsukare@ternaengg.ac.in "
    receiver_email = "ssukare74@gmail.com"
    password = "swapnil@1234"
    message = "Hello this was sent by using Python"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email,password)
    print("Login Success")
    server.sendmail(sender_email,receiver_email,message)
    print("Email has been seen to ", receiver_email)

def whatsapp():
    import pywhatkit
    pywhatkit.sendwhatmsg_instantly("+919082951297" , 'One face has been recognised')
    print("Whatsapp message has been sent")

def launch_ec2():
    import os
    os.system("aws ec2 run-instances  --image-id  ami-0ad704c126371a549 --instance-type t2.micro --key-name awsdef --count 1 ")

def creating_EBS_volume():
    import os
    os.system("aws ec2 create-volume --availability-zone ap-south-1a --size 5 --volume-type gp2")