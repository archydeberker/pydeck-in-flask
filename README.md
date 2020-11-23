# Pydeck in Flask

This is an example of plotting a [Pydeck](https://pydeck.gl/index.html) map in Flask.

It plots all (~1200) electric car charging stations in the UK. The data comes from 
[gov.uk]('https://www.gov.uk/guidance/find-and-use-data-on-public-electric-vehicle-chargepoints).

For another example, see Trip Carbon Calculator.  

## Installation

You can install dependencies with virtualenv and pip:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

I think for reliability you ought to get a token for [Mapbox](https://www.mapbox.com), but it's not
strictly necessary for this demo (I didn't do it.)

## Running

```bash
python app.py
```

You should see a map of the UK with lots of red (out of service) and green (in service) charging points.

