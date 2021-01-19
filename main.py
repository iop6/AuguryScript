import requests
import json

#Test query 10952004
url = "https://augury5.heliumrain.com/api"
payload = ""
headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "bef11806eb0dcbed79dfe0e94594b7322097907c"}
query_id = str(input("What is your query ID? "))

def Get_Flags():
  print("Starting the Flags function...")
  Flags = requests.request("GET", url+"/results/" + query_id + "?format=json&tcp_flags=194", data=payload, headers=headers)
  Flags_results = open("Flags.json", "w")
  Flags_results.write(Flags.text)
  Flags_results.close()

#-------------------------------------------------------------------------------------------------------------------------------------
def Get_Bi_Directional():

  print('------------------------------------------------')
  src_dst = []
  flipped_ips = []

  results = requests.request("GET", url+"/results/" + query_id + "?format=json&ip_addr=205.18.101.0%2F24%2C+205.18.102.0%2F24%2C+205.18.103.0%2F24%2C+205.18.104.0%2F24%2C+205.18.186.0%2F24%2C+205.18.187.0%2F24%2C+205.18.188.0%2F24%2C+205.18.64.0%2F24%2C+205.18.69.0%2F24%2C+205.18.71.0%2F24%2C+205.18.74.0%2F24%2C+205.18.96.0%2F24%2C+205.18.97.0%2F24%2C+205.18.99.0%2F24", data=payload, headers=headers)
  BD_results = open("Bi_Directional.json", "w")
  BD_results.write(results.text)
  BD_results.close()

  with open("Bi_Directional.json", "r") as f:
    for line in f:
      json_line = json.loads(line)
      timestamp = json_line["start_time"]
      src_ip = json_line["src_ip_addr"]
      dst_ip = json_line["dst_ip_addr"]
      line = src_ip + "   " + dst_ip
      src_dst.append(line)
      flipper = dst_ip + "   " + src_ip
      flipped_ips.append(flipper)
      for value in src_dst:
        if value == flipper:
          print(value)

  print('------------------------------------------------')

#-------------------------------------------------------------------------------------------------------------------------------------
def Get_Country_Codes():
  CountryCodes = requests.request("GET", url+"/results/" + query_id + "?format=json&cc=CN,HK,CZ,DE", data=payload, headers=headers)
  CC_results = open("CountryCodes.json", "w")
  CC_results.write(CountryCodes.text)
  CC_results.close()

  with open("Bi_Directional.json", "r") as f:
    for line in f:
        json_line = json.loads(line)
        src_ip = json_line["src_ip_addr"]
        src_port = str(json_line["src_port"])
        src_cc = json_line["src_cc"]
        dst_ip = json_line["src_ip_addr"]
        dst_port = str(json_line["dst_port"])
        dst_cc = json_line["dst_cc"]
        
        print(src_ip + " " + src_port + " " + " " + src_cc + "   " + dst_ip + " " + dst_port + " " + dst_cc)
#-------------------------------------------------------------------------------------------------------------------------------------

def iplookup():
  print("starting iplookup...")
  request = requests.request("GET", url+"/results/" + query_id + "?format=json&cc=CN,HK,CZ,DE", data=payload, headers=headers)
  iplookup = open("iplookup.json", "w")
  iplookup.write(request.text)
  iplookup.close()

  

#Get_Flags()
Get_Bi_Directional()
#Get_Country_Codes()
#iplookup()

