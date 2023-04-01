import os
import re
import random
import string
import requests
from bs4 import BeautifulSoup

# 파트 2: 포스팅 주제를 직접 입력받거나, 자동으로 추천받아 포스팅 주제를 생성하는 코드 추가하기
def get_user_topic():
    """사용자에게 직접 포스팅 주제를 입력받는 함수"""
    return input("포스팅할 주제를 입력하세요: ")

def generate_topic():
    """Google 검색을 통해 블로그 포스팅 주제를 추천하는 함수"""
    keyword = input("검색어를 입력하세요: ")
    res = requests.get(f"https://www.google.com/search?q={keyword}&num=10")
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    search_results = soup.select(".yuRUbf > a")
    result_titles = [result.text for result in search_results]
    result_links = [result.get("href") for result in search_results]
    return result_titles[0], result_links[0]

def get_blog_title():
    """포스팅 제목을 입력받는 함수"""
    choice = input("포스팅 주제를 자동 추천받으시겠습니까? (y/n)")
    if choice.lower() == "y":
        topic_title, _ = generate_topic()
        return topic_title
    else:
        return get_user_topic()
# 파트 3: 포스팅 제목과 내용을 저장할 폴더를 생성하는 코드 추가하기
def create_post_folder():
    """포스팅을 저장할 폴더를 생성하고, 폴더명과 생성일자를 반환하는 함수"""
    now = datetime.datetime.now()
    folder_name = f"{now.strftime('%Y-%m-%d')}_포스팅저장"
    os.makedirs(folder_name, exist_ok=True)
    return folder_name, now.strftime("%Y-%m-%d")

def generate_random_title():
    # Generate a random title using a list of adjectives and nouns
    adjectives = ["Amazing", "Interesting", "Fantastic", "Incredible", "Fabulous", "Wonderful", "Marvelous", "Magnificent", "Terrific", "Excellent"]
    nouns = ["Ideas", "Facts", "Things", "Ways", "Tips", "Tricks", "Techniques", "Strategies", "Methods", "Secrets"]
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

def generate_topic():
    # Ask the user for a topic
    topic = input("Enter a topic for the blog post: ")

    # Get the Google search results page for the topic
    res = requests.get(f"https://www.google.com/search?q={topic}&num=10")
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Get the search result titles and links
    search_results = soup.select(".yuRUbf > a")
    result_titles = [result.text for result in search_results]
    result_links = [result.get("href") for result in search_results]

    # Randomly select one of the search results
    # num_results = len(result_titles)
    # if num_results == 0:
    #     print("No search results found.")
    #     return None, None
    # else:
    #     choice = random.randint(0, num_results-1)
    #     return result_titles[choice], result_links[choice]
    # Randomly select one of the search results
    num_results = len(result_titles)
    if num_results == 0:
        print("No search results found.")
        return
    elif num_results == 1:
        choice = 0
    else:
        choice = random.randint(0, num_results-1)

    topic_title = result_titles[choice]
    topic_link = result_links[choice]

def ask_topic():
    # Ask the user for a topic
    topic = input("Enter a topic for the blog post: ")

    # Generate a title based on the topic
    words = topic.split()
    if len(words) > 1:
        # Use the first two words of the topic as the basis for the title
        title = f"{words[0].capitalize()} {words[1].capitalize()}"
    else:
        title = topic.capitalize()

    return title

def generate_topic_and_post():
    # Generate a blog post based on a randomly selected topic
    topics = ["AI의 미래", "빅데이터와 사회", "프로그래밍 언어 비교", "프로젝트 관리 방법", "스마트폰의 발전"]
    selected_topic = random.choice(topics)
    content_part1 = f"{selected_topic}에 대해 이야기해보겠습니다. "
    content_part2 = "이것은 일반적으로 알려져 있지 않지만, "
    content_part3 = "그럼에도 불구하고, "
    content_part4 = f"{selected_topic}이 중요한 이유는 "
    content_part5 = f"결론적으로, {selected_topic}에 대해 알아보았습니다."

    return content_part1 + content_part2 + content_part3 + content_part4 + content_part5

# 파트 4: 포스팅 내용을 파일로 저장하는 코드 수정하기 ##############################

def save_blog_post(title, content, folder_name):
    """블로그 포스팅 제목과 내용을 파일로 저장하는 함수"""
    index = 1
    filename = f"{title.replace(' ', '_').lower()}.txt"

    while os.path.exists(os.path.join(folder_name, filename)):
        filename = f"{title.replace(' ', '_').lower()}_{index}.txt"
        index += 1

    content = content.replace('\n', ' ')
    content = ' '.join(content.split())

    max_len = 3000
    if len(content) > max_len:
        pattern = r"([^.!?]*[^.!?])"
        matches = list(re.finditer(pattern, content[:max_len]))
        last_sentence_match = matches[-1] if matches else None

        if last_sentence_match:
            content_part1 = content[:last_sentence_match.end()].strip()
            content_part2 = content[last_sentence_match.end():].strip()
        else:
            content_part1 = content[:max_len]
            content_part2

# 무작위 포스팅 제목 생성 대신, 미리 주어진 주제에서 포스팅 제목 생성
# 주어진 주제를 기반으로 포스팅 제목을 생성하는 함수를 만들어보겠습니다. 
# 이 함수는 generate_topic_title() 이라고 이름짓겠습니다. 
# 이 함수는 주제 키워드를 입력받아 구글 검색을 통해 얻은 
# 첫 번째 검색 결과의 제목을 반환합니다.

def generate_topic_title(keyword):
    # Get the Google search results page
    res = requests.get(f"https://www.google.com/search?q={keyword}&num=10")
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Get the first search result title
    search_result = soup.select_one(".yuRUbf > a")
    result_title = search_result.text if search_result else None

    return result_title
# 이 함수를 사용하려면, generate_blog_post() 함수에서 무작위 제목 생성 대신 
# 주제를 먼저 물어보고, 그 주제에 대한 검색 결과 중 첫 번째 제목을 사용하도록 변경해야 합니다. 
# 이에 따라 generate_blog_post() 함수도 수정해보겠습니다

def generate_blog_post():
    # Ask for the blog post topic
    topic = input("어떤 주제로 포스팅을 작성하시겠습니까? ")

    # Generate a title based on the topic
    title = generate_topic_title(topic)
    if not title:
        print("검색 결과를 찾을 수 없습니다.")
        return None

    # Combine the content
    content_part1 = "This is the first part of the content. It contains some text that will be split across two files. "
    content_part2 = "This is the second part of the content, which continues from the first part."
    combined_content = content_part1 + content_part2

    # Save the blog post
    saved_files = save_blog_post(title, combined_content)
    if isinstance(saved_files, tuple):
        print(f"Blog post saved as {saved_files[0]} and {saved_files[1]}")
    else:
        print(f"Blog post saved as {saved_files}")

    # Generate keywords and tags based on the blog post content
    keywords = set(combined_content.split())
    tags = [f"<tag>{keyword}</tag>" for keyword in keywords]

    # Save the keywords and tags to the end of the blog post file
    if isinstance(saved_files, tuple):
        for filename in saved_files:
            with open(filename, "a", encoding="utf-8") as f:
                f.write("\n\nKeywords:\n")
                f.write(", ".join(keywords))
                f.write("\n\nTags:\n")
                f.write(" ".join(tags))
    else:
        with open(saved_files, "a", encoding="utf-8") as f:
            f.write("\n\nKeywords:\n")
            f.write(", ".join(keywords))
            f.write("\n\nTags:\n")
            f.write(" ".join(tags))

# 7. 자동 생성할 포스팅 주제를 물어보는 코드 추가
# 포스팅 제목과 내용을 주어진 주제를 생성하도록 하는 방법과, 
# 자동 생성할 주제를 물어보는 두 가지 방법을 추가할 수 있습니다.
# 먼저, 주어진 주제를 생성하는 방법에 대해 설명드리겠습니다. 
# 이를 위해서는 주제를 찾아내는 구글 검색 기능을 활용하여 검색 결과 중 
# 첫 번째 제목을 사용할 수 있습니다. 아래는 해당 기능을 추가한 코드 예시입니다.77
# 이 코드에서는 사용자로부터 주제를 입력받아 구글 검색 결과 중 
# 첫 번째 제목을 가져와 포스팅 제목으로 사용합니다. 
# 만약 주어진 주제로부터 생성된 제목이 없다면 해당 정보를 출력합니다.

def generate_title_from_topic(topic):
    # Get the Google search results page
    res = requests.get(f"https://www.google.com/search?q={topic}&num=10")
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Get the search result titles
    search_results = soup.select(".yuRUbf > a")
    result_titles = [result.text for result in search_results]

    # Return the first search result title
    return result_titles[0] if result_titles else None

def search_wikipedia(query):
    # Get the search results from Wikipedia
    search_results = wikipedia.search(query)

    # Randomly select one of the search results
    num_results = len(search_results)
    if num_results == 0:
        print("No search results found.")
        return None, ""
    else:
        choice = random.randint(0, num_results-1)
        result_title = search_results[choice]

    # Get the content of the selected Wikipedia page
    try:
        page = wikipedia.page(result_title)
        content = page.content
    except wikipedia.exceptions.DisambiguationError as e:
        # if the result title refers to disambiguation page, pick the first suggested page
        content = wikipedia.page(e.options[0]).content
    
    # Process the content into a short paragraph
    summary_sentences = summarize(content, SENTENCES_COUNT)
    content_part1 = ""
    content_part2 = ""
    if summary_sentences:
        content_part1 = summary_sentences[0]
    if len(summary_sentences) > 1:
        content_part2 = " ".join(summary_sentences[1:])

    return result_title, content_part2


# Example usage
topic = input("Enter a blog post topic: ")
generated_title = generate_title_from_topic(topic)
if generated_title:
    print(f"Generated title: {generated_title}")
else:
    print("Could not generate a title from the given topic.")




# 다음으로, 자동 생성할 주제를 묻는 방법을 추가할 수 있습니다. 
# 이를 위해서는 랜덤하게 주제를 생성하는 대신, 미리 정해둔 주제 목록 중 
# 하나를 물어보고 사용자의 응답에 따라 해당 주제를 사용하도록 할 수 있습니다. 
# 아래는 해당 기능을 추가한 코드 예시입니다.
# 이 코드에서는 미리 정해둔 주제 목록을 사용자에게 보여주고, 
# 사용자로부터 선택을 받아 해당 주제를 반환합니다. 만약 사용자가 잘못된 입력을 하거나
def get_topic_from_user():
    topic_list = [
        "How to improve your writing skills",
        "Tips for staying productive while working from home",
        "The benefits of meditation",
        "The importance of regular exercise",
        "How to start a successful blog"
    ]
    print("Choose a blog post topic from the following options:")
    for i, topic in enumerate(topic_list):
        print(f"{i+1}. {topic}")
    while True:
        try:
            choice = int(input("Enter the number of your chosen topic: "))
            if choice < 1 or choice > len(topic_list):
                raise ValueError
            return topic_list[choice-1]
        except ValueError:
            print("Invalid input. Please enter a valid topic number.")

# Example usage
chosen_topic = get_topic_from_user()
print(f"Chosen topic: {chosen_topic}")

# 이 코드에서는 무작위 주제와 내용을 생성하고 있습니다. 주어진 주제를 사용하려면 어떻게 해야 할까요?
# 답변: 주어진 주제를 사용하려면 generate_random_title() 함수 대신에 
# 주어진 주제를 반환하는 함수를 만들어야 합니다. 
# 예를 들어, 다음과 같이 코드를 수정할 수 있습니다.
def generate_specific_title(topic):
    # 주어진 주제를 반환하는 함수
    return topic.replace(' ', '_').lower()

# ...

if __name__ == "__main__":
    # 주어진 주제를 사용하도록 수정
    topic = "포스팅 주제"
    title = generate_specific_title(topic)
    print(f"제목: {title}")

    # 내용 결합
    content_part1 = "이것은 내용의 첫 번째 부분입니다. 두 개의 파일에 걸쳐 분할될 텍스트가 포함됩니다. "
    content_part2 = "이것은 두 번째 부분의 내용입니다. 첫 번째 부분에서 계속됩니다."
    combined_content = content_part1 + content_part2

    # 블로그 글 저장
    saved_files = save_blog_post(title, combined_content, folder_name="포스팅저장")
    if isinstance(saved_files, tuple):
        print(f"블로그 글이 {saved_files[0]} 및 {saved_files[1]}로 저장되었습니다.")
    else:
        print(f"블로그 글이 {saved_files}로 저장되었습니다.")

# 주제를 자동 생성하는 대신에, 사용자에게 주제를 물어보는 코드를 추가하고 싶습니다. 
# 어떻게 해야 할까요?
# 답변: 사용자에게 주제를 물어보려면, input() 함수를 사용하면 됩니다. 
# 예를 들어, 다음과 같이 코드를 수정할 수 있습니다.
if __name__ == "__main__":
    # 사용자로부터 주제 입력 받기
    topic = input("포스팅 주제를 입력하세요: ")
    
    # 7자리 무작위 제목 생성
    title = generate_random_title()
    print(f"생성된 제목: {title}")

    # 내용 결합
    content_part1 = "이것은 내용의 첫 번째 부분입니다. 두 개의 파일에 걸쳐 분할될 텍스트가 포함됩니다. "
    content_part2 = "이것은 두 번째 부분의 내용입니다. 첫 번째 부분에서 계속됩니다."
    combined_content = content_part1 + content_part2

    # 블로그 글 저장
    saved_files = save_blog_post(title, combined_content, folder_name="포스팅저장")
    if isinstance(saved_files, tuple):
        print(f"블로그 글이 {saved_files[0]} 및 {saved_files[1]}로 저장되었습니다.")
    else:
        print(f"블로그 글이 {saved_files}로 저장되었습니다.")


# 포스팅 제목과 내용을 생성할 때 사용할 주제 키워드 목록은 미리 제공되는 것인가요, 
# 아니면 코드 내에서 검색할 것인가요?
# 주제 키워드를 검색할 때, Google 검색 대신 다른 검색 엔진을 사용하거나, 
# 검색 

를 활용할 계획이 있나요?
# 자동 생성할 주제를 물어보는 코드를 작성할 때, 사용자가 입력한 단어나 문장을 
# 기반으로 추천 주제를 생성할 것인가요, 아니면 미리 정해놓은 주제 키워드를 활용할 것인가요?

def generate_title_from_topic(topic_title):
    # Generate a title from the topic by selecting random words
    title_words = topic_title.split()
    num_words = random.randint(3, 7)
    title = ' '.join(random.sample(title_words, num_words))
    return title

def generate_content_from_topic(topic_link):
    # Get the text from the first search result page
    res = requests.get(topic_link)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "html.parser")
    paragraphs = soup.find_all('p')

    # Select a random subset of paragraphs and combine them into a single string
    num_paragraphs = random.randint(3, 6)
    selected_paragraphs = random.sample(paragraphs, num_paragraphs)
    combined_content = ' '.join([paragraph.get_text() for paragraph in selected_paragraphs])

    return combined_content

# 파트 3: 포스팅 저장 함수 수정, 생성일 및 포스팅 번호를 파일명에 추가하는 코드 추가
def save_blog_post(folder_name,title, content):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Generate a unique filename
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{timestamp}_{title}.txt"

    # Write the blog post content to the file
    with open(os.path.join(folder_name, filename), "w", encoding="utf-8") as f:
        f.write(content)

    # Return the path of the saved file
    return os.path.join(folder_name, filename)
    # Create a directory for blog posts if it doesn't already exist
    if not os.path.exists("포스팅저장"):
        os.makedirs("포스팅저장")

    # Generate a unique filename for the post based on the current date and time
    now = datetime.now()
    post_date = now.strftime("%Y-%m-%d")
    post_number = len(os.listdir("포스팅저장")) + 1
    filename = f"포스팅저장/{post_date}-{post_number}-{title.replace(' ', '_').lower()}.txt"

    # Write the content to the file
    content = content.replace('\n', ' ')
    content = ' '.join(content.split())
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    return filename
# 파트 4: 주제를 묻고 포스팅을 자동 생성하는 함수를 만드는 코드
def generate_topic_and_post():
    # Ask the user for a topic
    topic = input("Enter a topic for the blog post: ")

    # Get the Google search results page for the topic
    res = requests.get(f"https://www.google.com/search?q={topic}&num=10")
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Get the search result titles and links
    search_results = soup.select(".yuRUbf > a")
    result_titles = [result.text for result in search_results]
    result_links = [result.get("href") for result in search_results]

    # Randomly select one of the search results
    num_results = len(result_titles)
    if num_results == 0:
        print("No search results found.")
        return
    elif num_results == 1:
        choice = 0
    else:
        choice = random.randint(0, num_results-1)
# 이번에는 주어진 주제를 이용해 블로그 포스트의 제목과 내용을 자동으로 
# 생성하는 코드를 추가해보겠습니다. 이를 위해, 검색어를 입력받고, Google 검색 
# 결과 페이지에서 해당 검색어와 관련된 첫 번째 결과를 이용하여 블로그 포스트의 
# 제목과 내용을 생성할 수 있습니다.

def generate_random_title():
    # 7자리 무작위 문자열 생성
    return ''.join(random.choices(string.ascii_lowercase, k=7))


def save_blog_post(title, content):
    index = 1
    filename = f"{title.replace(' ', '_').lower()}.txt"

    while os.path.exists(filename):
        filename = f"{title.replace(' ', '_').lower()}_{index}.txt"
        index += 1

    content = content.replace('\n', ' ')  # 모든 줄바꿈을 공백으로 대체
    content = ' '.join(content.split())   # 모든 중복 공백을 제거

    # 내용을 두 부분으로 나누기
    max_len = 3000
    if len(content) > max_len:
        # 3000자 제한 이전의 마지막 완전한 문장 찾기
        pattern = r"([^.!?]*[^.!?])"
        matches = list(re.finditer(pattern, content[:max_len]))
        last_sentence_match = matches[-1] if matches else None

        if last_sentence_match:
            content_part1 = content[:last_sentence_match.end()].strip()
            content_part2 = content[last_sentence_match.end():].strip()
        else:
            content_part1 = content[:max_len]
            content_part2 = content[max_len:]

        # 내용의 첫 부분 저장
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content_part1)

        # 내용의 두 번째 부분 저장
        index = 1
        while os.path.exists(f"{title}_{index}.txt"):
            index += 1
        filename_part2 = f"{title}_{index}.txt"
        with open(filename_part2, "w", encoding="utf-8") as f:
            f.write(content_part2)

        return filename, filename_part2
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return filename


def generate_topic():
    # Keyword to search for
    keyword = input("블로그 포스트 주제를 입력하세요: ")

    # Get the Google search results page
    res = requests.get(f"https://www.google.com/search?q={keyword}&num=10")
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Get the search result titles and links
    search_results = soup.select(".yuRUbf > a")
    result_titles = [result.text for result in search_results]
    result_links = [result.get("href") for result in search_results]

    # Return the first search result title and link
    return result_titles[0], result_links[0]

# 블로그 포스트 내용을 두 개의 파일로 분할하는 코드를 구현해보세요.

def generate_random_title():
    # 7자리 무작위 문자열 생성
    return ''.join(random.choices(string.ascii_lowercase, k=7))

def save_blog_post(title, content):
    index = 1
    folder_name = "포스팅저장"
    filename = f"{title.replace(' ', '_').lower()}.txt"
    folder_path = os.path.join(os.getcwd(), folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    filepath = os.path.join(folder_path, filename)

    while os.path.exists(filepath):
        filename = f"{title.replace(' ', '_').lower()}_{index}.txt"
        filepath = os.path.join(folder_path, filename)
        index += 1

    content = content.replace('\n', ' ')  # 모든 줄바꿈을 공백으로 대체
    content = ' '.join(content.split())   # 모든 중복 공백을 제거

    # 내용을 두 부분으로 나누기
    max_len = 3000
    if len(content) > max_len:
        # 3000자 제한 이전의 마지막 완전한 문장 찾기
        pattern = r"([^.!?]*[^.!?])"
        matches = list(re.finditer(pattern, content[:max_len]))
        last_sentence_match = matches[-1] if matches else None

        if last_sentence_match:
            content_part1 = content[:last_sentence_match.end()].strip()
            content_part2 = content[last_sentence_match.end():].strip()
        else:
            content_part1 = content[:max_len]
            content_part2 = content[max_len:]

        # 내용의 첫 부분 저장
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content_part1)

        # 내용의 두 번째 부분 저장
        index = 1
        while os.path.exists(os.path.join(folder_path, f"{title}_{index}_part2.txt")):
            index += 1
        filename_part2 = f"{title}_{index}_part2.txt"
        filepath_part2 = os.path.join(folder_path, filename_part2)
        with open(filepath_part2, "w", encoding="utf-8") as f:
            f.write(content_part2)

        return filepath, filepath_part2
    else:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return filepath

if __name__ == "__main__":
    # 주어진 주제 중에서 하나를 선택하여 블로그 글 내용 생성
    topics = ["AI의 미래", "빅데이터와 사회", "프로그래밍 언어 비교", "프로젝트 관리 방법", "스마트폰의 발전"]
    selected_topic = random.choice(topics)
    content_part1 = f"{selected_topic}에 대해 이야기해보겠습니다. "
    content_part2 = generate_topic_and_post()

    # 블로그 포스트 제목 생성
    generate_random = input("Would you like to generate a random title? (y/n): ")
    if generate_random.lower() == "y":
        title = generate_random_title()
        print(f"Generated title: {title}")
    else:
        title = input("Please enter a title for your blog post: ")

    # 블로그 포스트 내용 생성
    content = content_part1 + content_part2

    # 블로그 포스트 저장     ###############################
    def save_blog_post(title, content, folder_name="포스팅저장"):
        # Create the folder if it does not exist
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Generate a filename based on the post title
        filename = f"{title}.txt"

        # Write the content to the file
        with open(os.path.join(folder_name, filename), "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Blog post saved as {filename} in the {folder_name} folder.")
        return filename
        saved_files = save_blog_post(title, content)

    # 저장된 블로그 포스트 읽어오기
    for filename in saved_files:
        content = read_blog_post(filename)
        print(f"File name: {filename}")
        print(f"Content:\n{content}")

# 7.내용 분할 및 저장
def generate_random_title():
    # 7자리 무작위 문자열 생성
    return ''.join(random.choices(string.ascii_lowercase, k=7))

def save_blog_post(title, content, topic_title=None):
    now = datetime.datetime.now()

    # "포스팅저장" 폴더 생성
    if not os.path.exists("포스팅저장"):
        os.makedirs("포스팅저장")

    # 제목에서 특수문자 제거
    title = re.sub(r'[^\w\s]','', title)

    # 제목에 주제 추가
    if topic_title:
        title = f"{topic_title} - {title}"

    index = 1
    filename = f"포스팅저장/{now.strftime('%Y%m%d')}_{index:03d}_{title}.txt"

    # 파일명이 중복되지 않도록 인덱스 추가
    while os.path.exists(filename):
        index += 1
        filename = f"포스팅저장/{now.strftime('%Y%m%d')}_{index:03d}_{title}.txt"

    content = content.replace('\n', ' ')  # 모든 줄바꿈을 공백으로 대체
    content = ' '.join(content.split())   # 모든 중복 공백을 제거

    # 내용을 두 부분으로 나누기
    max_len = 3000
    if len(content) > max_len:
        # 3000자 제한 이전의 마지막 완전한 문장 찾기
        pattern = r"([^.!?]*[^.!?])"
        matches = list(re.finditer(pattern, content[:max_len]))
        last_sentence_match = matches[-1] if matches else None

        if last_sentence_match:
            content_part1 = content[:last_sentence_match.end()].strip()
            content_part2 = content[last_sentence_match.end():].strip()
        else:
            content_part1 = content[:max_len]
            content_part2 = content[max_len:]

        # 내용의 첫 부분 저장
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content_part1)

        # 내용의 두 번째 부분 저장
        index = 1
        while os.path.exists(f"포스팅저장/{now.strftime('%Y%m%d')}_{index:03d}_{title}_part2.txt"):
            index += 1
        filename_part2 = f"포스팅저장/{now.strftime('%Y%m%d')}_{index:03d}_{title}_part2.txt"
        with open(filename_part2, "w", encoding="utf-8") as f:
            f.write(content_part2)

        return filename, filename_part2
    else:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        return filename

if __name__ == "__main__":
    # 사용자로부터 주제 입력 받기
    topic_title = input("포스팅할 주제를 입력하세요: ")

# 사용자로부터 포스팅 제목과 내용을 입력받는 코드를 추가해보겠습니다. 
# 이를 위해 input() 함수를 사용합니다.
if __name__ == "__main__":
    # Generate a random title or ask for a specific one
    while True:
        generate_random = input("Would you like to generate a random title? (y/n): ")
        if generate_random.lower() == "y":
            title = generate_random_title()
            print(f"Generated title: {title}")
            break
        elif generate_random.lower() == "n":
            title = input("Please enter a title for your blog post: ")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # Recommend a blog post topic based on Google search or ask for a specific one
    generate_topic_option = input("Would you like a recommended blog post topic based on Google search? (y/n): ")
    if generate_topic_option.lower() == "y":
        topic_title, topic_link = generate_topic()
        print(f"Recommended blog post topic: {topic_title}")
        print(f"Link: {topic_link}")
    else:
        topic_title = input("Please enter a topic for your blog post: ")

    # Ask for blog post content
    content = input("Please enter the content for your blog post: ")

    # Save the blog post
    saved_files = save_blog_post(title, content)
    if isinstance(saved_files, tuple):
        print(f"Blog post saved as {saved_files[0]} and {saved_files[1]}")
    else:
        print(f"Blog post saved as {saved_files}")

# 요기 위가 포스팅을 자동으로 할지,  주제를 줄건지 물어본는 구간 과 자동저장 함


# 마지막으로, 저장된 블로그 포스트의 내용을 읽어오는 코드를 추가해보겠습니다.
def read_blog_post(filename):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    return content

if __name__ == "__main__":
    # Generate a random title or ask for a specific one
    generate_random = input("Would you like to generate a random title? (y/n): ")
    if generate_random.lower() == "y":
        title = generate_random_title()
        print(f"Generated title: {title}")
    else:
        title = input("Please enter a title for your blog post: ")

    # Recommend a blog post topic based on Google search or ask for a specific one
    generate_topic_option = input("Would you like a recommended blog post topic based on Google search? (y/n): ")
    if generate_topic_option.lower() == "y":
        topic_title, topic_link = generate_topic_and_post()
        print(f"Recommended blog post topic: {topic_title}")
        print(f"Link: {topic_link}")
    else:
        topic_title = input("Please enter a topic for your blog post: ")

    # Generate the content for the blog post
    content = generate_blog_post_content(topic_title)

    # Save the blog post to a file
    folder_name = "blog_posts"
    saved_files = save_blog_post(folder_name, title, content)
    print(f"Blog post saved to: {saved_files}")
    # Generate a random title or ask for a specific one
    generate_random = input("Would you like to generate a random title? (y/n): ")
    if generate_random.lower() == "y":
        title = generate_random_title()
        print(f"Generated title: {title}")
    else:
        title = input("Please enter a title for your blog post: ")

    # Recommend a blog post topic based on Google search or ask for a specific one
    generate_topic_option = input("Would you like a recommended blog post topic based on Google search? (y/n): ")
    if generate_topic_option.lower() == "y":
        topic_title, topic_link = generate_topic()
        print(f"Recommended blog post topic: {topic_title}")
        print(f"Link: {topic_link}")  # 요기 에러 물어볼것

    # Generate content for the blog post
    content = generate_content()

    # Save the blog post
    folder_name = "blog_posts"    
    saved_files = save_blog_post(folder_name, title, content)
    print(f"Blog post saved to {saved_files[0]} and {saved_files[1]}")
# 8번 포스팅 내용 중 일부를 이미지로 만들어서 함께 게시하는 코드를 추가해주시면 좋을 것 같습니다.
# 이를 위해서는 Python의 Pillow 라이브러리를 사용하여 이미지를 생성하고, 
# 이미지를 포함한 HTML 코드를 생성하여 블로그 글에 삽입하는 방법을 사용할 수 있습니다. 
# 예를 들어, 다음과 같은 코드를 사용할 수 있습니다:?
from PIL import Image, ImageDraw, ImageFont

def generate_image(text):
    # Create a new image with a white background
    font = ImageFont.truetype("arial.ttf", 20)
    width, height = font.getsize(text)
    image = Image.new("RGB", (width + 20, height + 20), "white")

    # Draw the text onto the image
    draw = ImageDraw.Draw(image)
    draw.text((10, 10), text, font=font, fill="black")

    return image

if __name__ == "__main__":
    # Generate an image from some text
    text = "This is some sample text."
    image = generate_image(text)

    # Save the image to a file
    image.save("image.png")

    # Generate HTML code to include the image in a blog post
    html = f'<img src="image.png" alt="{text}" width="{image.width}" height="{image.height}">'
    print(html)

# 이 코드는 입력된 텍스트로부터 이미지를 생성하고, 이미지를 PNG 파일로 저장합니다. 
# 그리고, 생성된 이미지를 포함한 HTML 코드를 생성하여 출력합니다. 
# 이렇게 생성된 HTML 코드를 블로그 글에 포함시키면 이미지와 함께 글을 작성할 수 있습니다.
# 이미지를 생성하는 방법은 다양합니다. Pillow 라이브러리를 사용하지 않고, 
# 다른 이미지 처리 라이브러리를 사용하거나, 이미지 생성 웹 서비스를 활용하여 
# 이미지를 생성할 수도 있습니다. 이 경우, 해당 라이브러리나 웹 서비스 API를 사용하여 
# 이미지를 생성하는 코드를 작성하고, 이를 위한 설정을 추가하여야 합니다.

# 8 주어진 주제를 생성하는 코드는 다음과 같이 작성할 수 있습니다.
def generate_topic():
    # API endpoint와 API key
    endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
    api_key = "" # 본인 api key

    # prompt 설정
    prompt = (
        "Please generate a blog post topic about machine learning.\n"
        "Topic:"
    )

    # API 호출
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {"prompt": prompt, "max_tokens": 50}
    response = requests.post(endpoint, headers=headers, json=data)

    # 결과 처리
    topic = response.json()["choices"][0]["text"].strip()
    return topic

# 자동으로 주제를 생성할지 물어보는 코드
def ask_topic():
    answer = input("Do you want to generate a blog post topic? (y/n): ")
    if answer.lower() == "y":
        return generate_topic()
    else:
        return input("Please enter a topic for the blog post: ")
# 이 코드는 사용자에게 주제를 생성할지 물어보고, "y"를 입력하면 generate_topic() 
# 함수를 호출하여 주제를 생성하고, "n"을 입력하면 주제를 수동으로 입력받는 코드입니다. 
# 만약 "y"나 "n" 이외의 값이 입력되면 ask_topic() 함수를 다시 호출합니다.
# 따라서 이전에 작성한 코드에서 generate_random_title() 함수를 ask_topic() 함수로 수정하고, 
# generate_topic() 함수를 추가하여 블로그 포스트의 주제를 자동으로 생성하도록 할 수 있습니다.
################################################################################
# ask_topic() 함수 작성
# ask_topic() 함수는 사용자에게 주제를 생성할지 물어보고, "y"를 입력하면 generate_topic() # 
# 함수를 호출하여 주제를 생성하고, "n"을 입력하면 주제를 수동으로 입력받는 함수입니다. 
# "y"나 "n" 이외의 값이 입력되면 ask_topic() 함수를 다시 호출합니다.
def ask_topic():
    choice = input("블로그 포스트 주제를 자동 생성하시겠습니까? (y/n): ")
    if choice.lower() == 'y':
        topic_title, topic_link = generate_topic()
        return topic_title
    elif choice.lower() == 'n':
        topic_title = input("블로그 포스트 주제를 입력하세요: ")
        return topic_title
    else:
        print("잘못된 입력입니다. 다시 입력해주세요.")
        return ask_topic()
# generate_topic() 함수 작성
# generate_topic() 함수는 Google 검색을 통해 블로그 포스트 주제를 자동으로 생성합니다. 
# 이전에 작성한 generate_topic() 함수에서 발생했던 문제를 해결하기 위해 User-Agent 
# 헤더를 추가하였습니다.
def generate_topic():
    # Keyword to search for
    keyword = "blog post topics"

    # Set User-Agent header to prevent Google from blocking the request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

    # Get the Google search results page
    res = requests.get(f"https://www.google.com/search?q={keyword}&num=10", headers=headers)
    res.raise_for_status()

    # Parse the HTML content
    soup = BeautifulSoup(res.text, "html.parser")

    # Get the search result titles and links
    search_results = soup.select(".yuRUbf > a")
    result_titles = [result.text for result in search_results]
    result_links = [result.get("href") for result in search_results]

    # Return the first search result title
    return result_titles[0]

# main 함수 수정
# main 함수에서는 ask_topic() 함수를 호출하여 주제를 생성하거나 수동으로 입력받아서 
# 사용자가 선택한 방식에 따라 블로그 포스트 주제를 설정합니다.
def main():
    topic = input("Enter a blog post topic: ")
    search_results = search_wikipedia(topic)

    if search_results is None:
        print("No search results found.")
        return

    search_results_preview = get_search_results_preview(search_results)

    print("Choose a blog post topic from the following options:")
    for i, result in enumerate(search_results_preview):
        print(f"{i+1}. {result}")

    while True:
        topic_option = input("Enter the number of your chosen topic: ")
        if not topic_option.isnumeric() or int(topic_option) < 1 or int(topic_option) > len(search_results_preview):
            print("Invalid input. Please enter a valid topic number.")
        else:
            chosen_topic = search_results[int(topic_option)-1]
            print(f"Chosen topic: {chosen_topic}")
            break

    post_title = input("Enter a title for the blog post: ")

    generate_topic_option = input("Would you like to generate a random title? (y/n): ")
    if generate_topic_option.lower() == "y":
        post_title = generate_title(chosen_topic)

    post_content = generate_post_content(chosen_topic)

    if post_content is not None:
        folder_name = input("Enter a folder name to save the blog post: ")
        saved_files = save_blog_post(folder_name, post_title, post_content)
        print(f"Blog post saved to the following file(s):\n{saved_files}")
    else:
        print("Blog post could not be generated.")
