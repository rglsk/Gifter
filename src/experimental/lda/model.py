from gifter.crawlers.suggested import *
from gifter.modeling.lda.lda import *
from gifter.modeling.models import BaseModel


class LdaModel(BaseModel):

    def __init__(self):
        super(LdaModel, self).__init__('LDA', 'storage_name')
        self.result = []
        self.texts2 = []

    def _get_storage(self):
        return

    def train(self, inputs, outputs):
        for df in inputs:
            self.texts2.append(list(
                itertools.chain(
                    *[df['lemmas'].irow(i) for i in range(df.shape[0])]
                )
            ))
        lda(
            list_of_json=self.texts2,
            save_model_as='lda.model',
            save_dic_as='dictionary.dic'
        )
        self.result = learned_categories(
            train=inputs,
            out=outputs,
            dictionary='dictionary.dic',
            lda='lda.model')
        return self.result

    def predict_one(self, one):
        """
        :param one: preprocessed twitter DataFrame
        """
        return self.result[
            find_topic(
                frame=one,
                dictionary='dictionary.dic',
                lda='lda.model'
                )[0][0]]

    def predict_many(self, inputs):
        """
        :param inputs: list of preprocessed twitter DataFrames
        """
        return [self.result[
            find_topic(
                frame=(i),
                dictionary='dictionary.dic',
                lda='lda.model'
                )[0][0]] for i in inputs]

if __name__ == '__main__':
    lda = LdaModel()
