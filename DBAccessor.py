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
        FROM LEAFSPY_RAW_TEST, ECOLOG_Doppler_NotMM
        WHERE LEAFSPY_RAW_TEST.DRIVER_ID = ECOLOG_Doppler_NotMM.DRIVER_ID
        AND LEAFSPY_RAW_TEST.DATETIME = ECOLOG_Doppler_NotMM.JST
        AND JST >= '2018-06-18 09:28:29.000'
        ORDER BY JST
        """

        rows = DBAccessor.ExecuteQuery(query)

        return rows
    
    @classmethod
    def SpeedDataDescription(self):
        query = """
        SELECT JST, SENSOR_ID,ECOLOG_Doppler_NotMM.SPEED
        FROM LEAFSPY_RAW_TEST, ECOLOG_Doppler_NotMM
        WHERE LEAFSPY_RAW_TEST.DRIVER_ID = ECOLOG_Doppler_NotMM.DRIVER_ID
        AND LEAFSPY_RAW_TEST.DATETIME = ECOLOG_Doppler_NotMM.JST
        AND JST >= '2018-06-18 09:28:29.000'
        ORDER BY JST
        """

        rows = DBAccessor.GetDescription(query)

        return rows

    @classmethod
    def TimeDistinctDataQuery(self):
        query = """
        SELECT DISTINCT JST, SPEED1 / 100.0, SPEED2 / 100.0
        FROM LEAFSPY_RAW_TEST, ECOLOG_Doppler_NotMM
        WHERE LEAFSPY_RAW_TEST.DRIVER_ID = ECOLOG_Doppler_NotMM.DRIVER_ID
        AND LEAFSPY_RAW_TEST.DATETIME = ECOLOG_Doppler_NotMM.JST
		AND JST >= '2018-06-18 09:28:29.000'
        ORDER BY JST
        """

        rows = DBAccessor.ExecuteQuery(query)

        return rows