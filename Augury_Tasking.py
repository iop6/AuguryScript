import requests
import json

url = "https://augury5.heliumrain.com/api"
payload = ""
headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "bef11806eb0dcbed79dfe0e94594b7322097907c"}

def Get_Flags():
  print("Starting the Flags function...")
  Flags = requests.request("GET", url+"/results/10952004?format=json&tcp_flags=194", data=payload, headers=headers)
  Flags_results = open("Flags.json", "w")
  Flags_results.write(Flags.text)
  Flags_results.close()

def Get_Bi_Directional():

  print('Start')
#------------------------------------------------------------------------------------------------#
  src_dst = []
#  results = requests.request("GET", url+"/results/10952004?format=json", data=payload, headers=headers)
#  BD_results = open("Bi_Directional.json", "r+")
#  BD_results.write(results)

  with open('Bi_Directional.json') as f:
    lines = f.read()
    for line in lines:
      json_line = json.loads(line)
      src_ip = json_line["src_ip_addr"]
      dst_ip = json_line["dst_ip_addr"]
      line = src_ip + "   " + dst_ip
      src_dst.append(line)
      flipped = dst_ip + "   " + src_ip
      for value in src_dst:
        if value == flipped:
          print(value)
#  BD_results.close()
#------------------------------------------------------------------------------------------------#
  print('Done')

def Get_Country_Codes():
  CountryCodes = requests.request("GET", url+"/results/10952004?format=json&cc=CN,HK,CZ,DE", data=payload, headers=headers)
  CC_results = open("CountryCodes.json", "w")
  CC_results.write(CountryCodes.text)
  CC_results.close()


#Get_Flags()
Get_Bi_Directional()
#Get_Country_Codes()

#curl --url 'https://augury5.heliumrain.com/api/results/10952004?format=csv&cc=CN,HK,CZ,DE' --request GET --header 'Content-Type: application/x-www-form-urlencoded' --header 'Authorization: bef11806eb0dcbed79dfe0e94594b7322097907c' > test.csv
