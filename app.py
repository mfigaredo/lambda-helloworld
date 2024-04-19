from chalice import Chalice
import time, requests

app = Chalice(app_name='helloworld')

@app.route('/')
def index():
    # sample_text = (
    #     "The squirrel was in charge of acorn muffins, the rabbit brought a basket of the freshest carrots, and the owl",
    #     "brewed a pot of the most aromatic tea. As the sun dipped below the horizon, casting a golden glow over the",
    #     "garden, laughter and chatter filled the air, creating a melody that even the stars above paused to listen to."
    # )
    # print('Running the index function')
    # return {'hello': 'galaxy', 'sample_text': sample_text}

    url = 'https://v2.jokeapi.dev/joke/Any'
    response = requests.get(url)
    data = response.json()
    if data['type'] == 'single':
        joke = data['joke']
    else:
        joke = f"{data['setup']}\n{data['delivery']}"
    time_asleep = 2
    time.sleep(time_asleep)
    return {
        'joke': joke,
        'time_taken': time_asleep,
    }

