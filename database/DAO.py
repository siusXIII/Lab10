from database.DB_connect import DBConnect
from model.arco import Arco
from model.country import Country


class DAO():

    @staticmethod
    def getAllCountries():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
                   FROM country c
                """

        cursor.execute(query)

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllNodes(idMap, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT distinct cc.StateAbb 
                   FROM country cc, contiguity ct
                   where ct.state1no = cc.CCode and ct.`year` <= %s
                   """

        cursor.execute(query, (anno, ))

        for row in cursor:
            result.append(idMap[row["StateAbb"]])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllEdges(idMap, anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select state1ab as s1, state2ab as s2
                   from contiguity c 
                   where c.`year`<= %s and c.conttype = 1"""

        cursor.execute(query, (anno,))

        for row in cursor:
            if row["s1"] in idMap and row["s2"] in idMap:
                result.append(Arco(idMap[row["s1"]], idMap[row["s2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVicini(country, anno):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """select count(*) as n 
                   from contiguity c
                   where c.state1ab  = %s and  c.`year` <= %s and c.conttype =1"""

        cursor.execute(query, (country, anno))

        result = cursor.fetchone()

        cursor.close()
        conn.close()
        return result
