import requests
import json

#Test query 10952004
url = "https://augury5.heliumrain.com/api"
payload = ""
headers = {"Content-Type": "application/x-www-form-urlencoded", "Authorization": "bef11806eb0dcbed79dfe0e94594b7322097907c"}

def Get_Flags():
  query_id = str(input("What is your query ID? "))
  print("Starting the Flags function...")
  Flags = requests.request("GET", url+"/results/" + query_id + "?format=json&tcp_flags=194", data=payload, headers=headers)
  Flags_results = open("Flags.json", "w")
  Flags_results.write(Flags.text)
  Flags_results.close()

#-------------------------------------------------------------------------------------------------------------------------------------
def Get_Bi_Directional():
  query_id = str(input("What is your query ID? "))

  print('------------------------------------------------')
  src_dst = []
  flipped_ips = []
  detailed_lines = []

  #Filter networks: &ip_addr=205.18.101.0%2F24%2C+205.18.102.0%2F24%2C+205.18.103.0%2F24%2C+205.18.104.0%2F24%2C+205.18.186.0%2F24%2C+205.18.187.0%2F24%2C+205.18.188.0%2F24%2C+205.18.64.0%2F24%2C+205.18.69.0%2F24%2C+205.18.71.0%2F24%2C+205.18.74.0%2F24%2C+205.18.96.0%2F24%2C+205.18.97.0%2F24%2C+205.18.99.0%2F24

  results = requests.request("GET", url+"/results/" + query_id + "?format=json", data=payload, headers=headers)
  BD_results = open("Bi_Directional.json", "w")
  BD_results.write(results.text)
  BD_results.close()

  with open("Bi_Directional.json", "r") as f:
    for line in f:
      json_line = json.loads(line)
      #All needed field for daily tasking.
      timestamp = json_line["start_time"]
      src_ip = json_line["src_ip_addr"]
      src_cc = json_line["src_cc"]
      dst_ip = json_line["dst_ip_addr"]
      dst_cc = json_line["dst_cc"]
      proto = str(json_line["proto"])
      src_port = str(json_line["src_port"])
      dst_port = str(json_line["dst_port"])
      tcp_flags = str(json_line["tcp_flags"])
      num_pkts = str(json_line["num_pkts"])
      num_octets = str(json_line["num_octets"])

      line = src_ip + "   " + dst_ip
      src_dst.append(line)

      flipper = dst_ip + "   " + src_ip
      flipped_ips.append(flipper)

      line_details = timestamp + "   " + src_ip + "   " + src_cc + "   " + proto + "   "  + dst_ip + "   "  + dst_cc + "   " + proto + "   " + dst_port + "   " + src_port + "   " + tcp_flags +                "   " + num_pkts + "   " + num_octets
      detailed_lines.append(line_details)

      # Need to iterate through line(first list) and compair that line # with the same line number in flipper (second list). If that item matches
      
      for value in src_dst:
        if value == flipper:
          print(value)
      '''
  i = 0
  for value1 in src_dst[i]:
    for value2 in flipped_ips[i]:
      if value1 == value2 and value2 == value1:
        print(detailed_lines[i])
    i += 1 
    '''
  print('------------------------------------------------')

#-------------------------------------------------------------------------------------------------------------------------------------
def Get_Country_Codes():
  query_id = str(input("What is your query ID? "))
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
  query_id = str(input("What is your query ID? "))
  print("starting iplookup...")
  request = requests.request("GET", url+"/results/" + query_id + "?format=json", data=payload, headers=headers)
  iplookup = open("iplookup.json", "w")
  iplookup.write(request.text)
  iplookup.close()

def Augury_Hunting():
  print('------------------------------------------------')
  query_ids = []
  hunted_ips = []
  looper1 = False 
  looper2 = False
  while looper1 == False:
    query_id = str(input("Type in query numbers you wish to look at: \n(Type " + '"done" when complete)\n'))
    while looper2 == False:
      query_ids.append(query_id)
      query_id = input()
      if query_id == "done":
        looper2 = True
    looper2 = False
    while looper2 == False:
      hunted_ip = str(input("What IP(s) are you looking for? \n(Type " + '"done" when complete)\n'))
      while looper2 == False:
        hunted_ips.append(hunted_ip)
        hunted_ip = input()
        if hunted_ip == "done":
          looper2 = True
    looper1 = True

  hunting = open("hunting_results.json", "w")
  for id in query_ids:
    results = requests.request("GET", url+"/results/" + id + "?format=json", data=payload, headers=headers)
    hunting = open("hunting_results.json", "a")
    hunting.write(results.text)
    hunting.close()
  print('\n------------------------------------------------')




#Get_Flags()
#Get_Bi_Directional()
#Get_Country_Codes()
#iplookup()
Augury_Hunting()


