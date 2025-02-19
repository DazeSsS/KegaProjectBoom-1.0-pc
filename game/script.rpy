﻿# начало игры
label start:

    stop music fadeout 2

    scene black

    "z-z-z..."

    scene bg classroom
    with fade

    show teacher

    t "Александр к доске! Вы вздумали спать, на уроке."

    hide teacher
    show dima glitched at right2

    d "Эй, Сашка, тебя к доске."

    show sanya at left2

    s "*зевает*"
    s "Да не спал я, просто глаза на секунду закрыл."

    hide sanya
    hide dima glitched
    show teacher

    t "Оно и видно *смешок*"
    t "Выходи давай, Саш."

    hide teacher
    show sanya

    "Мда, спать на уроке математики было конечно не лучшей идеей, и моя последняя парта первого ряда меня не спасла."
    s "Какая у нас там тема?"

    show sanya at left2
    show dima glitched at right2

    d "Повезло тебе, у нас пока что повторение."
    d "Квадратные уравнения."

    s "А, так это проще простого, сейчас все решу."

    hide sanya
    hide dima glitched

    scene bg board
    
    show teacher at left2

    t "Саш, будь добр, реши уравнение на доске."

    show sanya at right2

    s "Без проблем, Екатерина Петровна."

    hide sanya
    hide teacher

    call task from _call_task

    jump after_task

# решение уравнения
label task:
    
    show screen quest1

    window hide

    pause

    return

# проверка правильности решения уравнения
label check_answer:

    if place1 == "line2" and place2 == "line3":
        $ task_solved = True

    if task_solved:
        jump sanya_smart
    else:
        jump sanya_stupid

    return

# уравнение решено верно
label sanya_smart:

    show teacher at left2
    show sanya at right2

    # $ renpy.notify(NOTICE)
    $ intellect += 1

    if first_try:

        t "Даже спящий хорошо соображаешь, гений математики."
        s "Очень приятно, Екатерина Петровна."
        t "Садись, сейчас будет важная информация."

    else:

        t "Умничка, справился. Садись, сейчас будет важная информация."

    return

# уравнение решено неверно
label sanya_stupid:

    show teacher at left2
    show sanya at right2

    if first_try:

        t "Так и не проснулся. Ладно, растрепанный и сонный ты очень мило выглядишь, поэтому сегодня без плохой оценки, но, Саш, относись более отвественно к урокам."

        menu:
            "Мило выгляжу? Екатерина Петровна, прошу вас не подкатывать к ученикам, хотя бы на уроках.":

                # $ renpy.notify(NOTICE)
                $ charisma += 1

                t "Ахахах, с чувством юмора проблем у тебя нет. Так уж и быть, на уроках не буду."
                t "Садись, Саш, сейчас будет важная информация."

            "Не не, это недоразумение, давайте я переделаю, я не глупый, просто растерялся.":

                t "Ну хорошо, даю тебе последний шанс"

                hide sanya
                hide teacher

                $ first_try = False

                jump task

            "Соблюдайте субординацию. Вы же учитель.":

                # $ renpy.notify(NOTICE)
                $ bad_point += 1

                t "Шуток не понимаешь, садись."

    else:

        t "Сегодня просто не твой день, Саш."
        t "Садись, сейчас будет важная информация."
        
    return

# после выхода к доске
label after_task:

    scene bg classroom

    "По пути к парте я окинул взглядом класс."
    "Школы нового типа крайне приятны на вид. Небо и земля по сравнению с обычными."
    "Какие же стильные все-таки голографические проекторы."

    show teacher

    t "Итак, ребята. Важное объявление, наша школа включена в программу профориентации будущего, поэтому ученики 11 классов пройдут специальное тестирование."
    "Голос из класса" "Это будет как тест, что мы писали в 10 классе?"
    "Голос из класса" "100 вопросов, от которых скорее утонешь, чем поймешь кто ты."
    t "Нет конечно, не перебивайте. Сейчас расскажу поподробнее."
    t "Завтра мы едем в главное здание компании Neurotech."
    t "Там вы пообщаетесь с разработчиками, и они представят вам проект “Твой Путь”."
    t "Этот проект использует технологию прямой трансляции, с помощью которой определят ваши склонности и таланты."
    t "Поэтому это вам не тесты из 10 класса."
    t "Больше мне, увы, ничего не сказали."
    t "А, ну и явка обязательна."
    t "Встречаемся завтра в 10 утра у школы, Neurotech организовывает нам трансфер до штаб квартиры."
    t "У вас есть вопросы?"

    show sanya at right2
    show teacher at left2

    menu:
        "Что такое технология прямой трансляции?":

            $ intellect += 1
            # $ renpy.notify(NOTICE)

            "Голос из класса" "Как такое можно не знать?"
            t "Так, каждый из нас может не знать многое, главное что Саша интересуется."
            t "На самом деле у меня самой не очень много информации."
            t "Neurotech сильно усовершенствовала технологию трансляции информации человеку прямо в мозг, наверное вы следили за экспериментами."
            t "В общем, с помощью этой технологии проведут анализ вас, считают данные мозга и найдут дело, которое лучше всего вам подходит."

            show teacher at left2
            show sanya at right2

            s "Спасибо, Екатерина Петровна."

            hide teacher

        "*промолчать*":

            s "Да все понятно."

            hide teacher

    show sanya at left2
    show dima glitched at right2

    s "“Твой Путь” ну и название."
    s "Что-то менее пафосное и сектантское не могли придумать."
    d "Не бухти. Мы попадем в здание мегакорпорации и познакомимся с новейшим продуктом."
    d "Это уникальная возможность, спасибо новому министерству образования."
    s "Да мне просто непонятны названия, как будто мы в игре какой-то."
    s "Ладно, Neurotech значит, и кто это?"
    d "М-да, ты о них не слышал? Погоди, ты серьезно?"
    s "Ну слышать то слышал конечно, наши Ar очки в конце концов от них, но на этом мои познания заканчиваются."
    s "Большая компания, делают свои примочки и делают."
    d "Как бы ты совсем от жизни не отстал с таким подходом, если интересно то могу рассказать о том, что сейчас в мире происходит."
    s "Ну давай."
    d "Ага, так я тебе все и рассказал."
    d "У нас урок заканчивается, а если все тебе говорить, то разговор минимум на часа 4."
    d "Дружище, у нас есть интернет, посмотри все сам. Или потом можем встретится у тебя на работе."

    "*звенит звонок*"

    d "И за чашечкой бесплатного чая я выдам тебе жесткое эссе про наш дивный мир."
    s "Платного."
    d "Информация в обмен на чай, по моему выгодная сделка."
    d "Ладно, до вечера!"
    s "Пока, пока."

    hide dima glitched with Dissolve(1)
    show sanya at center

    "Голограмма Димы растворилась, голографический проектор над партой выключился, а вслед за ним и остальные, кто был онлайн на уроке, отключились."
    "Мне бы тоже сейчас оказаться дома в тепле и уюте, а не идти по улице в дождь."
    "Почему родителям так важно чтобы я очно ходил в школу?"

    scene bg school_outside
    with fade

    "*саша выходит на улицу и надевает свои очки дополненной реальности*"

    i "Здравствуй, Alex. На улице 10 градусов, дождь, ветер 12 мс, влажность 97%%, вероятность осадков 99%%."
    i "По предварительным данным погода будет ухудшаться."

    show sanya

    s "Мда, погода не из приятных."

    jump go_home

# урок закончился и Саша собирается домой
label go_home:  

    menu:
        "Куда же дальше?"

        "Осмотреть школу" if school_info:
        
            $ school_info = False

            s "Информация о школе."
            i "ТОГ №3. Технологическое образовательное учреждение."
            i "Одна из девяти школ “нового типа”, что появилась при изменении системы образования."
            i "Школы такого типа оснащены передовой техникой и позволяют осуществлять гибридный формат обучения."
            s "Эх, сейчас бы гибридно обучатся. Я ****."
            "*легкий удар током от смарт браслета*"
            i "Включена блокировка нецензурной лексики."
            s "Большое спасибо за родительский контроль на очках, а смарт браслет от очков не отключить."
            s "Ладно, насмотрелся я на мою высокотехнологичную школу, вроде бы школа будущего, а туалеты нормальные до сих пор сделать не могут."
            s "Уроками нагружают так, будто я две вышки сразу получаю, так еще и находится она на окраине города, так что добираться до нее полтора часа."
            s "Хотя бы при выпуске можно сразу среднее специальное получить, ну и кормят вкусно."
            s "Может домой? Или нет?"

            jump go_home
    
        "Немного пройтись":
        
            "Погода весьма поэтичная, да и дождь мне нравится, полюбуюсь видами."
            
            show sanya at left2
            show man at right2
            
            "Незнакомец" "Только плодов дерева, которое среди рая, сказал Бог, не ешьте их и не прикасайтесь к ним, чтобы вам не умереть."
            "Незнакомец" "Прокляты мы,  все мы прокляты. Не внемли мы господу нашему."

            "Передо мной был человек, лет так 60 с длинными грязными седыми волосами и такой же седой бородой."
            "Одет в потертые джинсы и грязную бежевую куртку на голое тело, на руках рваные перчатки. При себе лишь один рюкзак и книга в руках."

            s "Так, шизы рядом со школой это что-то новое."
            i "Внимание, при сканировании объекта обнаружено взрывное устройство, службы быстрого реагирования уже вызвано, ближайшие организации уведомлены об опасности, просьба максимально удалиться от объекта."
            "Незнакомец" "Мальчик. Стой мальчик."
            
            "Пора валить, и очень быстро."

            "*неожиданно незнакомец оказывается подле саши и хватает его за плечо*"

            "Незнакомец" "Мы прокляты, мы все прокляты. Мы пытаемся стать богами и за это господь уничтожит нас."
            s "Убери руки, быстро."

            "Лицо незнакомца было в шрамах и ссадинах, на груди была вытатуирована икона. Он был слеп на один глаз, а второй был искусственным."

            "Незнакомец" "Прости мальчик, я не хотел тебе навредить. Ты еще чист, не то что я."

            menu:
                "Ударить":

                    "После мощного удара в челюсть незнакомец издал истошный вскрик и попятился."

                    "Незнакомец" "Мальчик…"

                    "*из закрытого глаза незнакомца скатывается слеза*"

                    "Незнакомец" "Уходи, уходи."

                    "*звук выстрела*"

                    i "Объект был поражен транквилизатором, уровень опасности понижен. Проход гражданских на территорию возобновлен"
                    i "Пожалуйста не подходите к задержанному, скоро за ним приедут службы правопорядка."

                    "*Саша протер рукой холодный пот со лба.*"

                    "Что это вообще было?"

                    s "Алиса, такси до дома и как можно скорее."
                    i "К вам подъедет BMW Smart One с подпиской на дополнительный комфорт. Номер машины УУ454У."
                    s "Здорово, главное чтобы быстрее подъехало."

                    "*такси подъезжает и Саша садится в него*"

                    s "Фух..."
                    i "У вас сильно повышен пульс. Можете взять прохладную воду из мини холодильника, можно включить массаж сидения."
                    s "Нет, ничего не нужно."
                    i "Хорошо."
                
                "Отойти":

                    "Незнакомец" "Не играй в бога мальчик, не играй в бога."

                    "*звук выстрела*"

                    i "Объект был поражен транквилизатором, уровень опасности понижен. Проход гражданских на территорию возобновлен"
                    i "Пожалуйста не подходите к задержанному, скоро за ним приедут службы правопорядка."
                    s "Алиса, такси до дома и как можно скорее."
                    i "К вам подъедет BMW Smart One с подпиской на дополнительный комфорт. Номер машины УУ454У."
                    s "Здорово, главное чтобы быстрее подъехало."

                    "*такси подъезжает и Саша садится в него*"

                    s "Фух..."
                    i "У вас сильно повышен пульс. Можете взять прохладную воду из мини холодильника, можно включить массаж сидения."
                    s "Нет, ничего не нужно."
                    i "Хорошо." 

        "Заказать такси":

            s "Все, пора домой."
            s "Алиса, такси до дома."
            i "К вам подъедет BMW Smart One с подпиской на дополнительный комфорт. Номер машины УУ454У."
            i "Время ожидания 5 минут."

            "*Саша залипает в ТикТоке*"
            "*Подъезжает машина, он садится в нее*"

            "Ох, до сих пор не могу привыкнуть к отсутствию водителя на переднем сидении."
            "Как-то стремно ездить в беспилотных авто. Хотя количество аварий после их внедрения снизилось колоссально."
            "Даже подумывают о запрете вождения людям в городской местности."

            "Голос из передней панели такси" "Вы в машине, приступаю к исполнению заказа. Приятной поездки."
    
    scene bg road1 with fade

    "..."
    i "Рассказать анекдот?"

    menu:
        "Ну давай":

            jump jokes

        "Нет":

            i "Точно точно?"

            menu:
                "Ладно, давай.":

                    jump jokes

                "Да, давай без анекдотов.":

                    i "Хорошо, тогда не буду вас отвлекать."

                    scene bg road2 with fade

                    ""

                    jump at_home

# адекдоты в машине
label jokes:

    label first_joke:
        
        i "Итак. Внимание анекдот!"
        i "В поезде едут три программиста."
        s "Хм"
        i "У юзеров 3 билета, у программистов 1.\nЗаходит контроллёр."
        i "Юзеры показывают билеты, программисты прячутся в туалет."
        i "Контроллёр стучится в туалет, оттуда высовывается рука с билетом.\nПрограммисты едут дальше."
        i "На обратном пути. У юзеров 1 билет, у программистов ни одного."
        i "Заходит контроллёр."
        i "Юзеры прячутся в туалет. Один из программистов стучит, из туалета высовывается рука с билетом."
        i "Программисты забирают билет и прячутся в соседний туалет."
        i "Юзеров ссаживают с поезда."
        i "Вывод - не всякий алгоритм, доступный программисту, доступен юзеру."

        menu:
            "*посмеяться*":

                $ funny_jokes += 1 

                s "Неплохо. Давай еще один."
                i "Давайте."

                jump second_joke

            "Что-то не зашло...":

                i "Очень жаль, давайте еще один, следующий вам точно понравится."
                
                menu:
                    "Ну давай.":

                        jump second_joke
                    
                    "Нет, спасибо.":

                        i "Хорошо."

                        scene bg road2 with fade

                        jump feedback
    
    label second_joke:

        i "Заходит однажды тестировщик в бар. Забегает в бар. Пролезает в бар.\nТанцуя, проникает в бар. Крадется в бар. Врывается в бар."
        i "Прыгает в бар и заказывает: кружку пива, 2 кружки пива, 0 кружек пива, 999999999 кружек пива, ящерицу в стакане, -1 кружку пива, qwertyuip кружек пива."
        s "Проверяет все возможности."
        i "Первый реальный клиент заходит в бар и спрашивает, где туалет.\nБар вспыхивает пламенем и все погибают."

        menu:
            "Ха-ха-ха":

                $ funny_jokes += 1

                s "Это было прекрасно, ахахахах. Давай еще."
                i "Давайте."

                jump third_joke

            "Мда...":

                i "Очень жаль, что вам не понравилось, могу рассказать анекдот на другую тему."

                menu:
                    "Ладно, давай":

                        jump third_joke

                    "Пожалуй, хватит.":

                        i "Как скажете."

                        scene bg road2

                        jump feedback

    label third_joke:

        scene bg road2 with fade

        i "Идет заседание в рейстаге, присутствуют Гитлер, Гимлер, Мюллер. Заходит Штирлиц, ставит на стол поднос с апельсинами, берет из сейфа документы и уходит."
        i "Гитлер в гневе: - Это кто?\nГимлер и Мюллер в один голос: - Это русский разведчик Исаев."
        i "Гитлер: - Так, арестуйте его!\n- Бесполезно. Скажет, что апельсины приносил…"

        menu:
            "Ха-ха-ха-ха":

                $ funny_jokes += 1

                i "Рада слышать ваш смех."
            
            "Как-то не очень...":

                i "Хорошо, я учту ваше чувство юмора."
            

    label feedback:

        if funny_jokes == 3:

            s "Спасибо большое за прекрасные анекдоты."
            i "Рада стараться. У вас замечательное чувство юмора."
        
        else:

            i "Я очень сожалею о том, что вам не понравились анекдоты. Обещаю, в следующий раз вам понравится."

            menu:
                "Да ничего страшного, просто у меня чувство юмора такое. Спасибо за старание.":

                    # $ renpy.notify(NOTICE)
                    $ charisma += 1
                
                "Надеюсь":

                    # $ renpy.notify(NOTICE)
                    $ bad_point += 1

        jump at_home

# Саша приехал домой
label at_home:

    scene bg street with Fade(1, 1, 1)

    i "Мы приехали. Стоимость поездки 350 цифровых рублей."
    i "Деньги будут списаны с вашего счета. Программа такси приостановлена, очки переведены в обычный режим."
    s "Пора домой, пора домой."

    "Хм, чем бы заняться как приду, погода не располагает к поездкам и прогулкам, поиграть что-ли? Уроки?"

    scene bg flat with fade

    show sanya at right2
    show woman at left2

    s "Привет, мам."
    m "Привет, сынок."
    m "Еда если что в холодильнике."
    s "Да я не голоден, вот только устал что-то..."
    s "Пойду прилягу."
    
    hide sanya
    hide woman


    scene bg room with fade
    show sanya

    "Легкий запах дождя в квартире и небольшая прохлада. Есть все таки что-то хорошее в дождливой погоде, но и то, уже дома."   
    "Наконец-то любимая мягкая кровать. Надо бы погуглить про технологии…"

    scene black
    with fade

    "z-z-z..."
    "Внутренний голос" "Что вершит судьбу человечества в этом мире?"
    "Внутренний голос" "Некое незримое существо или закон, подобно Длани Господней парящей над миром?"
    "Внутренний голос" "По крайнер мере истинно лишь одно."
    "Внутренний голос" "Хей, хей, а мало ляма номиналом..."
    "Внутренний голос" "Итак, господа, сегодня мы отправляемся в плаванье?"
    "Внутренний голос" "В какое плавание?"
    "Внутренний голос" "На остров сокровищ."

    scene bg room with fade
    show sanya

    s "Так, какой остров сокровищ, чуть не уснул."
    s "Пронесло, а то дневной сон…"

    show sanya at right2
    show woman at left2

    m "Сынок, вставай, вставай."
    s "Что? Куда вставать?"
    m "Тебе сегодня ехать в компанию Neurotech."
    s "Сегодня?"
    m "Да, а что такое?"
    s "Сколько я спал…"
    m "Соня мой, быстрее собирайся. Я закажу тебе такси."

    jump coming_to_Neurotech