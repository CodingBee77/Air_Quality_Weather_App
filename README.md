# Air Quality App

A simple air quality application based on the Airly APIs:
[Airly](https://airly.org/pl/)

It returns information about current air pollution in every place
in the world (where Airly sensors are installed). 


The air quality index used in Europe, CAQI, has five ranges,
with the values presented on a scale from 0 (very low) to >100 (very high). 
It is a relative measure of the amount of air pollution.

To show the differences in air pollution, a colored 7-level scale 
operates on a website. Starts with green,
which indicates very good quality air and graduates all the way
to maroon which exceeds all air quality norms.


![](Air_quality_weather_app.gif)


## How to run project


**Clone the code**

Obtain the url to your git repository.

```
git clone https://github.com/CodingBee77/Python_projects.gitt
```

### Option 1 - use Docker

After cloning the repo, go to the app directory with the Dockerfile and:

```
 docker-compose up
```

After a few seconds, open your web browser to http://localhost:0.0.0.0. 
You should see our app!


### Option 2 - create virtual env and install all dependencies

**Creating the environment**

Create a virtual python environment for the project. If you're not using virtualenv you may skip this step.


**For virtualenv**


```
cd Python_projects/Air_Quality_Weather_App
virtualenv cd Air_Quality_Weather_App-env
cd Air_Quality_Weather_App-env/
source bin/activate
```

**Install requirements**

```
cd ..
pip install -r requirements.txt
```

**Add .env file**
 
Need to create file .env to Air_Quality_Weather_App/weather
with your own generated AIRLY_API_KEY=''

[Generate it here](https://developer.airly.org/docs)

**Running**

```
python manage.py runserver
```

Open browser to http://127.0.0.1:8000



##Important:
Please set a coordinates in format (coordinates do not contain more than 6 decimal places):

           49.986894,20.0648207

without a space between.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU](https://www.gnu.org/licenses/gpl-3.0.html)