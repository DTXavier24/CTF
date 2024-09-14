import ast
import requests
import time
from collections import defaultdict
import networkx as nx

def extract_coordinates(data):
    try:
        start_idx = data.index(':') + 1
        stop_idx = data.index('<')
        coordinates_str = data[start_idx:stop_idx].strip()
        coordinates = ast.literal_eval(coordinates_str)
        return coordinates
    except (ValueError, SyntaxError) as e:
        print(f"Error parsing coordinates: {e}")
        return None

def can_draw_single_line(coordinates):
    graph = nx.Graph()
    for pair in coordinates:
        point1, point2 = map(tuple, pair)
        graph.add_edge(point1, point2)
    
    return "Yes" if nx.has_eulerian_path(graph) else "No"

def get_response():
    cookies = {
    'PHPSESSID': 'e93e13b870dc89c6129afb4f3047822c',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,th;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Content-Length': '0',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=e93e13b870dc89c6129afb4f3047822c',
        'DNT': '1',
        'Origin': 'http://192.168.59.128',
        'Referer': 'http://192.168.59.128/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
    }

    response = requests.post('http://192.168.59.128/', cookies=cookies, headers=headers, verify=False)
    return response.text

def submit_response(txt):
    cookies = {
    'PHPSESSID': 'e93e13b870dc89c6129afb4f3047822c',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,th;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        # 'Cookie': 'PHPSESSID=e93e13b870dc89c6129afb4f3047822c',
        'DNT': '1',
        'Origin': 'http://192.168.59.128',
        'Referer': 'http://192.168.59.128/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36',
    }

    data = {
        'oneline_drawable': txt,
    }

    response = requests.post('http://192.168.59.128/', cookies=cookies, headers=headers, data=data, verify=False)
    return response.text

def main():
    while True:
        response_text = get_response()
        if 'FSIIEC' in response_text:
            print(response_text)
            break
        coordinates = extract_coordinates(response_text)
        if coordinates:
            drawable_status = can_draw_single_line(coordinates)
            submit_response_text = submit_response(drawable_status)
            
            if 'Wrong answer' in submit_response_text:
                print("Wrong Answer received, trying again...")
        else:
            print("Error processing data, skipping this round.")
        time.sleep(0.1)

if __name__ == "__main__":
    main()
