from rest_framework import serializers
from rooms.models import Room

from scheduling.models import Scheduling
from users.serializers import UserReturnSerializer
from rooms.serializers import RoomSerializer

class SchedulingSerializer(serializers.ModelSerializer):
    user = UserReturnSerializer(read_only=True)

    class Meta:
        model = Scheduling
        fields = ['id','scheduling_date','scheduling_start','scheduling_end','room','user']

    def create(self, validated_data):
        all_schedules = Scheduling.objects.all()
        msg = {'message': 'the room is already occupied at this time'}

        if validated_data['scheduling_start'] > validated_data['scheduling_end']:
            msg = {'message': 'the schedule end can not be lower than the schedule start.'}
            raise serializers.ValidationError(msg)

        for value in all_schedules:
            print(value.room)
            print(self.data)
            print(validated_data)
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

class SchedulingReturnSerializer(serializers.ModelSerializer): 
    user = UserReturnSerializer(read_only=True)

    class Meta:
        model = Scheduling
        fields = ['id','scheduling_date','scheduling_start','scheduling_end','room','user']
        depth = 1
