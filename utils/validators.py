from django.core.exceptions import ValidationError


def ValidateDates(date_start, date_end, date, validated_data, serializers):
    if (
        validated_data["scheduling_date_start"] < date.today()
        or validated_data["scheduling_date_end"] < date.today()
    ):
        err_msg = {
            "message": "Não é possível fazer um agendamento em dias antes de hoje."
        }
        raise serializers.ValidationError(err_msg)

    if date_start.weekday() == 5 or date_start.weekday() == 6:
        err_msg = {"message": "Não é possível fazer um agendamento no fim de semana."}
        raise serializers.ValidationError(err_msg)

    if date_end.weekday() == 5 or date_end.weekday() == 6:
        err_msg = {"message": "Não é possível fazer um agendamento no fim de semana."}
        raise serializers.ValidationError(err_msg)

    if validated_data["scheduling_date_start"] > validated_data["scheduling_date_end"]:
        err_msg = {
            "message": "O horário final do agendamento não pode ser menor que o horário inicial."
        }
        raise serializers.ValidationError(err_msg)
