import glob
import requests

def get_feedbacks():
    feedbacks = []
    for infiles in glob.glob("/data/feedback/*.txt"):
        with open(infiles, 'r') as i:
            txt = [line.strip() for line in i.readlines()]
            feedback = {
                'title': txt[0],
                'name': txt[1],
                'date': txt[2],
                'feedback': txt[3],
            }
            feedbacks.append(feedback)
    return feedbacks

def post_feedback(feedback):
    r = requests.post('http://34.170.162.40/feedback/', data=feedback)
    r.raise_for_status()

def main():
    feedbacks = get_feedbacks()
    for feedback in feedbacks:
        post_feedback(feedback)

if __name__ == "__main__":
    main()
