from rest_framework import serializers

from scheduling.models import Scheduling

class SchedulingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduling
        fields = ['id','scheduling_date','scheduling_start','scheduling_end','room']

    def create(self, validated_data):
        all_schedules = Scheduling.objects.all()
        msg = {'message': 'the room is already occupied at this time'}

        if validated_data['scheduling_start'] > validated_data['scheduling_end']:
            msg = {'message': 'the schedule end can not be lower than the schedule start.'}
            raise serializers.ValidationError(msg)

        for value in all_schedules:
            if value.scheduling_date == validated_data['scheduling_date']:
                if value.room == validated_data['room']:
                    if value.scheduling_start == validated_data['scheduling_start'] or validated_data['scheduling_end'] <= value.scheduling_end :
                        if validated_data['scheduling_start'] >= value.scheduling_start and validated_data['scheduling_start'] < value.scheduling_end:
                            raise serializers.ValidationError(msg)
                        raise serializers.ValidationError(msg)

        user = self.context['request'].user

        validated_data['user'] = user

        schedule = Scheduling.objects.create(**validated_data)

        return schedule
            