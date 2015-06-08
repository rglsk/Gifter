from gifter.crawlers.suggested import *
from gifter.modeling.lda.lda import *
from gifter.modeling.models import BaseModel
from gifter.modeling.evaluation.separate import separeted_data


class LdaModel(BaseModel):

    def __init__(self):
        super(LdaModel, self).__init__('LDA', 'storage_name')
        (self.inputs_train, self.inputs_test, self.output_train,
            self.output_test) = separeted_data(0.9)
        self.result = []

    def _get_storage(self):
        return

    def train(self, inputs, outputs):
        train_list = []
        for train_path in self.inputs_train['preprocessed_filename']:
            train_list = train_list + [train_path]
        """lda(
            list_of_json=train_list,
            save_model_as='lda.model',
            save_dic_as='dictionary.dic'
        )"""
        self.result = learned_categories(train=train_list)
        return self.result

    def predict_one(self, one):
        """
        :param one: preprocessed twitter DataFrame
        """
        return self.result[find_topic(frame=one)[0][0]]

    def predict_many(self, inputs):
        """
        :param inputs: list of preprocessed twitter DataFrames
        """
        return [self.result[find_topic(frame=(i))[0][0]] for i in inputs]

if __name__ == '__main__':
    lda = LdaModel()
