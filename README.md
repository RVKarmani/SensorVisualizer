# SensorVisualizer
A flask based web application to visualise data from a sensor based system - Arduino
Developed for a gas concentration sensor(MQ2) to get the ppm values of carbon monoxide and methane
[Made from the repository](https://github.com/feklistoff/cs50-final-project)

### Requirements
1. Flask
2. Flask-SocketIO
3. Flask-SQLAlchemy
4. pyserial
5. gevent
6. plotly

### Details

1. MQ2 sensor with Arduino UNO - Analog pin connection
2. PySerial takes the methane and CO ppm values from the sensor
2. Python Threading for storing data in SQLITE database and socket for getting real time data for plotting
3. sqlite3 with Flask-SQLAlchemy wrapper
4. Using plotly for plotting different graphs
5. Can view historical data of the 2 gases fetched from the database.

### Scripts

1. `helpers.py`- For offline plotting of the 2 gases
2. `models.py` - For the database structure
3. `arduino.py` - Driver code
4. `script2.py` - For taking 25 values from air and store in database
