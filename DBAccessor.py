import pyodbc

class DBAccessor:
    """DB Access"""

    config = "DRIVER={SQL Server};SERVER=ECOLOGDB2016;DATABASE=ECOLOGDBver3"
    @classmethod
    def ExecuteQuery(self, query):
        cnn = pyodbc.connect(self.config)
        cur = cnn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        cnn.close()
        return rows

    @classmethod
    def GetDescription(self, query):
        cnn = pyodbc.connect(self.config)
        cur = cnn.cursor()
        cur.execute(query)
        description = cur.description
        cur.close()
        cnn.close()
        return description

    @classmethod
    def SpeedDataQuery(self):
        query = """
        SELECT JST, SENSOR_ID,ECOLOG_Doppler_NotMM.SPEED
        FROM LEAFSPY_RAW3 as LEAFSPY, ECOLOG_Doppler_NotMM
        WHERE LEAFSPY.DRIVER_ID = ECOLOG_Doppler_NotMM.DRIVER_ID
        AND LEAFSPY.DATETIME = ECOLOG_Doppler_NotMM.JST
        AND JST >= '2018-07-11 09:00' AND JST <= '2018-07-11 11:00'
        ORDER BY JST
        """

        rows = DBAccessor.ExecuteQuery(query)

        return rows
    
    @classmethod
    def SpeedDataDescription(self):
        query = """
        SELECT JST, SENSOR_ID,ECOLOG_Doppler_NotMM.SPEED
        FROM LEAFSPY_RAW3 as LEAFSPY, ECOLOG_Doppler_NotMM
        WHERE LEAFSPY.DRIVER_ID = ECOLOG_Doppler_NotMM.DRIVER_ID
        AND LEAFSPY.DATETIME = ECOLOG_Doppler_NotMM.JST
        AND JST >= '2018-06-18 09:28:29.000'
        ORDER BY JST
        """

        rows = DBAccessor.GetDescription(query)

        return rows

    @classmethod
    def TimeDistinctDataQuery(self):
        query = """
        SELECT DISTINCT JST, SPEED1 / 100.0, SPEED2 / 100.0
        FROM LEAFSPY_RAW3, ECOLOG_Doppler_NotMM
        WHERE LEAFSPY_RAW3.DRIVER_ID = ECOLOG_Doppler_NotMM.DRIVER_ID
        AND LEAFSPY_RAW3.DATETIME = ECOLOG_Doppler_NotMM.JST
        AND JST >= '2018-07-11 09:00' AND JST <= '2018-07-11 11:00'
        ORDER BY JST
        """

        rows = DBAccessor.ExecuteQuery(query)

        return rows

    @classmethod
    def SpeedDataQuery2(self):
        query = """
        SELECT ECOLOG.JST, ECOLOG.SENSOR_ID,ECOLOG.SPEED, CAST(LEAFSPY.SPEED1/100.0 as float), CAST(LEAFSPY.SPEED2/100.0 as float), GPS.ACCURACY
        FROM LEAFSPY_RAW3 as LEAFSPY, ECOLOG_Doppler_NotMM as ECOLOG, CORRECTED_GPS_Doppler_NotMM as GPS
        WHERE LEAFSPY.DRIVER_ID = ECOLOG.DRIVER_ID
        AND LEAFSPY.DATETIME = ECOLOG.JST
        AND ECOLOG.JST >= '2018-06-18 09:28:29.000' AND GPS.SENSOR_ID = ECOLOG.SENSOR_ID AND GPS.JST = ECOLOG.JST
        ORDER BY ECOLOG.JST
        """

        rows = DBAccessor.ExecuteQuery(query)

        return rows