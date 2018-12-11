# EC601_project_3
simply run assignment_1.py is ok.<br/>
Data will be uploaded to database.<br/>

# Building Evironment
``Python 3.6``
``FFmpeg``
``Goole-Vision-API on Google Cloud Platform.``
``PIL``
``Tweepy``
``urllib``
``_mysql``
``pymongo``

# User Guide
tweetAPI.py is used to grab pictures from specified accounts.run by
```python
python tweetAPI.py
```
(Path is predefined in files)

GetAnnotation.py is used to get annotations for the pictures with goole-vision-api. and then add those annotations into those pictures with python PIL. Finnaly convert those pictures into a video with ffmpeg.<br/>
run by 
```python
python GetAnnotation.py
```
(the input and out_put path is predefined.)

assignment1.py is a file that import the previous python files and can be seen as a API.
just run like ```python python assignment1.py``` or open a new python file and <br/>```import assignment1.py```<br/>
```assignment1.Assign1("Your target account",'output_path','input_path','Labeled_imgs_path','Output_Video_Path')```<br/> is ok to run the API.

```python
python query_api_mysql.py
```

```python
python query_api_mongo.py
```
Above are apis for database querying.
