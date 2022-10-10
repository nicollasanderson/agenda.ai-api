from rest_framework import serializers
from rooms.models import Room
from datetime import date, datetime, time

from utils.validators import ValidateDates
from scheduling.models import Scheduling
from users.serializers import UserReturnSerializer
from rooms.serializers import RoomSerializer


class SchedulingSerializer(serializers.ModelSerializer):
    user = UserReturnSerializer(read_only=True)

    class Meta:
        model = Scheduling
        fields = [
            "id",
            "scheduling_date_start",
            "scheduling_date_end",
            "scheduling_time_start",
            "scheduling_time_end",
            "description",
            "is_active",
            "room",
            "user",
        ]
        read_only_fields = ["is_active"]

    def create(self, validated_data):
        time_start = validated_data["scheduling_time_start"]
        time_end = validated_data["scheduling_time_end"]

        time_start = time(int(time_start[:2]), int(time_start[3:5]))
        time_end = time(int(time_end[:2]), int(time_end[3:5]))

        validated_data["scheduling_time_start"] = time_start
        validated_data["scheduling_time_end"] = time_end

        all_schedules = Scheduling.objects.all()

        err_msg = {"message": "the room is already occupied at this time"}

        date_start = datetime.strptime(
            str(validated_data["scheduling_date_start"]), "%Y-%m-%d"
        )
        date_end = datetime.strptime(
            str(validated_data["scheduling_date_end"]), "%Y-%m-%d"
        )

        ValidateDates(date_start, date_end, date, validated_data, serializers)

        for value in all_schedules:
            if value.scheduling_date_start == validated_data["scheduling_date_start"]:
                if value.room == validated_data["room"]:
                    if (
                        value.scheduling_time_start
                        == validated_data["scheduling_time_start"]
                        or validated_data["scheduling_time_end"]
                        <= value.scheduling_time_end
                    ):
                        if (
                            validated_data["scheduling_time_start"]
                            >= value.scheduling_time_start
                            and validated_data["scheduling_time_start"]
                            < value.scheduling_time_end
                        ):
                            raise serializers.ValidationError(err_msg)
                        raise serializers.ValidationError(err_msg)

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
            "scheduling_date_start",
            "scheduling_date_end",
            "scheduling_time_start",
            "scheduling_time_end",
            "description",
            "is_active",
            "room",
            "user",
        ]
        depth = 1
