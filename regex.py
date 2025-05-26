import re 
# Practice Extract All Url's from text 

txt = """
Check out my website: https://www.example.com  
Visit our blog at http://blog.example.org/articles  
Or follow us on social: www.facebook.com/ourpage  
Also: https://youtube.com/watch?v=abc123
Invalid: http//broken.com, example_com
"""

pattern = r"(https?://[^\s]+|www\.[^\s]+)"

matches = re.findall(pattern, txt)

for urls in matches:
    print(urls)

