from mock_data import uyap_raw_log

raw_text = uyap_raw_log

# 1 - Function Definiton
def parse_uyap_log(raw_text):

    
    # 2 - Cleaning
    # 3 - Extraction
    raw_text = raw_text.replace("[SİSTEM UYARISI]","").strip().split("|")


    # print(raw_text)
        
    
    # 4 - Data Structuring
    parse_data = {}
    parse_data["Case_No"] = raw_text[0]
    parse_data["Status"] = raw_text[2]
    


    # 5 - Return
    return parse_data


parsed_result = parse_uyap_log(uyap_raw_log)

# 6 - Execution
print(parsed_result)

# 7 - print -> {'Case_No': 'Dosya: 2026/1050 ', 'Status': ' Durum: BEKLEMEDE'}