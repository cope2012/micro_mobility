import MySQLdb


def update_db(instance):
    if instance.__class__.__name__ == 'Scooter':
        db = MySQLdb.connect(user="test", passwd="TestUser2020!", db="mobility-test")
        c = db.cursor()
        c.execute(
            """UPDATE scooter SET 
            needs_charge = %s, 
            current_speed = %s, 
            status = %s,
            battery = %s 
            WHERE id = %s""",
            (
                instance.needs_charge,
                instance.current_speed,
                instance.status,
                instance.battery, 
                instance.id
            )
        )
        db.commit()
        c.close()
