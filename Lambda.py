import json
import boto3
s3=boto3.client('s3')
iam=boto3.client('iam')
ec2=boto3.client('ec2')
ec2_resource=boto3.resource("ec2")
def lambda_handler(event, context):
    # TODO implement
    #list all bucket
    if(event['type']=='s3-list'):
        name=[]
        buckets=s3.list_buckets()
        names=buckets['Buckets']
        for xx in names:
            name.append(xx["Name"])
        dc={'BucketNames':name}
        
    #Create User
    elif(event['type']=='iam-user'):
        dc=[]
        iam.create_user(UserName="newname",Tags=[
        {
        "Key":"Department",
        "Value":"IT"
        }

        ])
        iam.create_login_profile(UserName="newname",Password="Welcome@1234",PasswordResetRequired=False)
        response=iam.create_access_key(UserName="newname")
        access_key=response["AccessKey"]["AccessKeyId"]
        info={}
        secret_access_key=response["AccessKey"]["SecretAccessKey"]
        info={'userid':access_key,'usersecret':secret_access_key}
        dc.append(info)
        
    #Delete User
    elif(event['type']=='iam-deleteuser'):
        iam.delete_login_profile(UserName="newname")
        iam.delete_access_key(UserName="newname",AccessKeyId="AKIA5MWOI63C5LLDFX4C")
        iam.delete_user(UserName="newname")
    
    #list all users
    elif(event['type']=='iam-list'):
        user=[]
        users=iam.list_users()
        names=users['Users']
        for xx in names:
            user.append(xx['UserName'])
        dc={'UserNames':user}
    
    #list all ec2
    elif(event['type']=='ec2-list'):
        instance_id=[]
        instance_data=ec2.describe_instances()
        names=instance_data['Reservations']
        for xx in names:
            ins=xx['Instances']
            for xxx in ins:
                instance_id.append(xxx['InstanceId'])
            dc={'InstanceIds':instance_id}
            
    #list ec2 state
    elif(event['type']=='ec2-state'):
        dc=[]
        x=ec2.describe_instances()
        data=x['Reservations']
        for xx in data:
            datas=xx['Instances']
            info={}
            for info in datas:
                ec2_state=(info['State']['Name'])
                ec2_id=(info['InstanceId'])
                info={'Ec2id':ec2_id,'Ec2state':ec2_state}
                dc.append(info)
            
        
    
    
    #start instance
    elif(event['type']=='ec2-start'):
        ec2_state=[]
        ec2_id=[]
        x=ec2.describe_instances()
        data=x['Reservations']
        for xx in data:
            datas=xx['Instances']
            for info in datas:
                stanstate=info['State']['Name']
                stanid=info['InstanceId']
                if stanstate=='stopped':
                    ec2.start_instances(InstanceIds=[stanid])
    
     #stop instance
    elif(event['type']=='ec2-stop'):
        ec2_state=[]
        ec2_id=[]
        x=ec2.describe_instances()
        data=x['Reservations']
        for xx in data:
            datas=xx['Instances']
            for info in datas:
                stanstate=info['State']['Name']
                stanid=info['InstanceId']
                if stanstate=='running':
                    ec2.stop_instances(InstanceIds=[stanid])
            
    elif(event['type']=='s3-deletebucket'):
        response=s3.list_buckets()
        buckets=response["Buckets"]
        for xx in buckets:
            s3.delete_bucket(Bucket=xx['Name']) 
    
    
    #create ec2 instance
    elif(event['type']=='ec2-instance'):
        ec2_resource.create_instances(ImageId='ami-0aa7d40eeae50c9a9',
            InstanceType='t2.micro',MaxCount=1,MinCount=1)
    return {
        'statusCode': 200,
        'body': event
    }