from django.core.exceptions import ValidationError


def ValidateDates(date_start, date_end, date, validated_data, serializers):
    if (
        validated_data["scheduling_date_start"] < date.today()
        or validated_data["scheduling_date_end"] < date.today()
    ):
        err_msg = {"message": "its not possible to make a schedule before today."}
        raise serializers.ValidationError(err_msg)

    if date_start.weekday() == 5 or date_start.weekday() == 6:
        err_msg = {"message": "its not possible to make a schedule in the weekend."}
        raise serializers.ValidationError(err_msg)

    if date_end.weekday() == 5 or date_end.weekday() == 6:
        err_msg = {"message": "its not possible to make a schedule in the weekend."}
        raise serializers.ValidationError(err_msg)

    if validated_data["scheduling_date_start"] > validated_data["scheduling_date_end"]:
        err_msg = {
            "message": "the schedule end can not be lower than the schedule start."
        }
        raise serializers.ValidationError(err_msg)
