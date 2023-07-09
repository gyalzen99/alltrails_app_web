from app.models.things_to_do.things_to_do_model import ThingsToDoModel


class ThingsToDoService:
    def getData(
        self,
        things_to_do_object: ThingsToDoModel,
    ):
        title = things_to_do_object.title
        culture_tour = things_to_do_object.culture_tour.all()
        food_tour = things_to_do_object.food_tour.all()
        treak = things_to_do_object.treak.all()

        data = {
            'title': title,
            'culture_tours': culture_tour,
            'food_tours': food_tour,
            'treaks': treak,
        }

        return data
