from flask import Flask, jsonify
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

# Set up database connection
DATABASE_URL = "postgresql://postgres:rfiTbos%4012@localhost:5432/ny_airquality"  # URL-encoded '@' as '%40'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)


@app.route('/data', methods=['GET'])
def get_data() :
    session = Session()  # Create a session per request
    try :
        # Sample query to fetch data (modify based on your table)
        result = session.execute(text(
            "SELECT uniqueid, indicatorid, name, measureinfo, geotypename, geoplacename, timeperiod, date, datavalue FROM environmentaldata"))

        # Convert each row to a dictionary using ._mapping to access row as dictionary-like structure
        data = [dict(row._mapping) for row in result]
    finally :
        session.close()  # Ensure the session is closed after use

    return jsonify(data)


if __name__ == '__main__' :
    app.run(port=5000, debug=True)