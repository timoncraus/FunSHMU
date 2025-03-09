from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField, RadioField
from wtforms.validators import DataRequired


class Test(FlaskForm):
    q1 = RadioField(label='Как ты любишь проводить время?', choices=['общаясь с друзьями', 'за чтением книги', 'за компьютером', 'на природе'],
                    render_kw={'class': 'radio-label'})
    q2 = RadioField(label='Вы поехали в путешествие заграницу. Какое место вы бы посетили в первую очередь?', choices=['национальный парк',
                                                                                                                       'старинную библиотеку или знаменитый книжный магазин',
                                                                                                                       'любое, где можно пообщаться с местными жителями',
                                                                                                                       'офис крупной IT-компании или какой-нибудь IT-воркшоп'],
                    render_kw={'class': 'radio-label'})
    q3 = RadioField(label='Ты обычно...', choices=['проявляешь общительность', 'ведёшь себя спокойно'],
                    render_kw={'class': 'radio-label'})
    q4 = RadioField(label='Тебя скорее можно назвать:', choices=['человеком практичным', 'выдумщиком, романтиком'],
                    render_kw={'class': 'radio-label'})
    q5 = RadioField(label='Школа в первую очередь должна:', choices=['учить общению с другими детьми', 'давать знания', 'обучать навыкам работы'],
                    render_kw={'class': 'radio-label'})
    q6 = RadioField(label='Какие методы изучения тебе нравятся больше всего?', choices=['моделирование', 'анализ', 'наблюдение', 'описание'],
                    render_kw={'class': 'radio-label'})
    bool1, bool2, bool3, bool4, bool5, bool6, bool7, bool8, = BooleanField(label='работа на секретном объекте'), \
                                                              BooleanField(label='работа в лаборатории'), \
                                                              BooleanField(label='выпуск актуальных продуктов'),\
                                                              BooleanField(label='общение с большим количеством людей'),\
                                                              BooleanField(label='помощь людям'),\
                                                              BooleanField(label='изучение планеты'), \
                                                              BooleanField(label='работа с документами'), \
                                                              BooleanField(label='разработка игр')
    
    submit = SubmitField('Отправить', render_kw={'class': 'log_in_btn'})
