from rest_framework import serializers
from rooms.models import Room
from datetime import datetime

from scheduling.models import Scheduling
from users.serializers import UserReturnSerializer
from rooms.serializers import RoomSerializer


class SchedulingSerializer(serializers.ModelSerializer):
    user = UserReturnSerializer(read_only=True)

    class Meta:
        model = Scheduling
        fields = [
            "id",
            "scheduling_date",
            "scheduling_start",
            "scheduling_end",
            "room",
            "user",
        ]

    def create(self, validated_data):
        all_schedules = Scheduling.objects.all()
        msg = {"message": "the room is already occupied at this time"}

        date = datetime.strptime(str(validated_data["scheduling_date"]), "%Y-%m-%d")

        if date.weekday() == 5 or date.weekday() == 6:
            msg = {"message": "its not possible to make a schedule in the weekend."}
            raise serializers.ValidationError(msg)

        if validated_data["scheduling_start"] > validated_data["scheduling_end"]:
            msg = {
                "message": "the schedule end can not be lower than the schedule start."
            }
            raise serializers.ValidationError(msg)

        for value in all_schedules:
            print(value.room)
            print(self.data)
            print(validated_data)
            if value.scheduling_date == validated_data["scheduling_date"]:

                if value.room == validated_data["room"]:
                    if (
                        value.scheduling_start == validated_data["scheduling_start"]
                        or validated_data["scheduling_end"] <= value.scheduling_end
                    ):
                        if (
                            validated_data["scheduling_start"] >= value.scheduling_start
                            and validated_data["scheduling_start"]
                            < value.scheduling_end
                        ):
                            raise serializers.ValidationError(msg)
                        raise serializers.ValidationError(msg)

        user = self.context["request"].user

        validated_data["user"] = user

        schedule = Scheduling.objects.create(**validated_data)

        return schedule


class SchedulingReturnSerializer(serializers.ModelSerializer):
    user = UserReturnSerializer(read_only=True)

    class Meta:
        model = Scheduling
        fields = [
            "id",
            "scheduling_date",
            "scheduling_start",
            "scheduling_end",
            "room",
            "user",
        ]
        depth = 1
