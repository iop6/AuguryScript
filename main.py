import requests
import json

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

def Get_Bi_Directional():

  print('Start')
#------------------------------------------------------------------------------------------------#
  src_dst = []
  flipped_ips = []
  
  #results = requests.request("GET", url+"/results/10952004?format=json", data=payload, headers=headers)
  results = requests.request("GET", url+"/results/" + query_id + "?format=json", data=payload, headers=headers)
  BD_results = open("Bi_Directional.json", "w")
  BD_results.write(results.text)
  BD_results.close()

  with open("Bi_Directional.json", "r") as f:
    for line in f:
      json_line = json.loads(line)
      src_ip = json_line["src_ip_addr"]
      dst_ip = json_line["dst_ip_addr"]
      line = src_ip + "   " + dst_ip
      src_dst.append(line)
      flipper = dst_ip + "   " + src_ip
      flipped_ips.append(flipper)
      for value in src_dst:
        if value == flipper:
          print(value)
        
#------------------------------------------------------------------------------------------------#
  print('Done')

def Get_Country_Codes():
  CountryCodes = requests.request("GET", url+"/results/" + query_id + "?format=json&cc=CN,HK,CZ,DE", data=payload, headers=headers)
  CC_results = open("CountryCodes.json", "w")
  CC_results.write(CountryCodes.text)
  CC_results.close()


#Get_Flags()
Get_Bi_Directional()
#Get_Country_Codes()

