import requests
import time


class StackOverflow:
    def get_latest_questions(self):
        todate = int(time.time())
        fromdate = todate - 172800
        total_questions_list = []
        url = "https://api.stackexchange.com/2.3/questions?fromdate=" + f"{fromdate}" + "&todate=" + f"{todate}" + \
              "&order=desc&sort=creation&tagged=python&site=stackoverflow&filter=total"
        response = requests.get(url)
        print(f"За последние 2 дня было {response.json()['total']} вопросов с тэгом 'Python'")
        pages_quantity = response.json()['total'] // 100 + 1
        for page in range(1, pages_quantity + 1):
            url = "https://api.stackexchange.com/2.3/questions?page=" + f"{page}" + "&pagesize=100&fromdate=" + \
                  f"{fromdate}" + "&todate=" + f"{todate}" + "&order=desc&sort=creation&tagged=python&site=stackoverflow"
            response = requests.get(url)
            json_data = response.json()
            questions_list = json_data['items']
            total_questions_list.extend(questions_list)
            for question in questions_list:
                print(question['title'])
        return len(total_questions_list)  # проверка


if __name__ == '__main__':
    compilation = StackOverflow()
    print(compilation.get_latest_questions())
