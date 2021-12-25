import json
import jsonschema
from typing import Dict
from config import SCHEMA_CONF_FILE, INPUT_FILE, logger, LOGGING_LEVEL


class Event():
    def __init__(self) -> None:
        pass

    @staticmethod
    def get_schema() -> dict:
        ''' Gets the defined schema specification
        Parameters
        ----------
        None

        Returns
        -------
        Schema Specification
        '''
        with open(SCHEMA_CONF_FILE, 'r') as fp:
            schema = json.load(fp)
        return schema

    @staticmethod
    def validate_schema(event, schema) -> None:
        ''' Validates the schema of the event object against the schema specification
        Parameters
        ----------
        event:
            event object from the input file
        schema:
            schema specification object
        Returns
        -------
        None
        '''
        jsonschema.validate(instance=event, schema=schema,
                            format_checker=jsonschema.FormatChecker())

    @staticmethod
    def generate_report(event_count) -> None:
        ''' Generates a report for the count of each event occuring for each date in the data
        Parameters
        ----------
        event_count
            count of events per date
        Returns
        -------
        None
        '''
        print('\nEvent Count Report')
        print('--------------------------------------------------------------')
        print('        Date               | Count   |  Event Name')
        print('---------------------------------------------------------------')
        for date, event in event_count.items():
            for name, count in event.items():
                print("{0} |   {2}     | {1}".format(date, name, count))
        print('---------------------------------------------------------------')

    def count_events(self) -> None:
        ''' Reads the input file and counts the events occuring for each date in the data
        Parameters
        ----------
        None

        Raises
        ------
        jsonschema.exceptions.ValidationError

        Returns
        -------
        None
        '''
        schema = self.get_schema()
        event_count = dict()
        with open(INPUT_FILE, 'r') as fp:
            for e in fp:
                event = json.loads(e)
                try:
                    self.validate_schema(event, schema)
                except jsonschema.exceptions.ValidationError as err:
                    logger.log(LOGGING_LEVEL, err.message)
                if event['received_at'] in event_count:
                    if event['event'] in event_count[event['received_at']]:
                        event_count[event['received_at']
                                    ][event['event']] += 1
                    else:
                        event_count[event['received_at']
                                    ][event['event']] = 1
                else:
                    event_count[event['received_at']] = {
                        event['event']: 1}
        self.generate_report(event_count)

    def run(self) -> None:
        ''' Driver Method '''
        self.count_events()


if __name__ == '__main__':
    event_obj = Event()
    event_obj.run()
