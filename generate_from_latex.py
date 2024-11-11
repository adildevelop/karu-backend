from pylatex import Document, Command, Package, TextBlock, NoEscape

from umk import Umk

def generateDokladnoiFromLatex(name, date, faculty, dean, department, group, lesson_name, start_time, end_time):
    # Basic document
    geometry_options = {"margin": "0.5in"}
    doc = Document(geometry_options=geometry_options)
    doc.change_length("\TPHorizModule", "1mm")
    doc.change_length("\TPVertModule", "1mm")
    doc.packages.append(Package('babel', options=['russian']))

    doc.append(Command('fontsize', arguments=['14', '12']))
    doc.append(Command('selectfont'))

    with doc.create(TextBlock(70, 135, 0)):
        doc.append(f'Декану факультета {faculty}\n')
        doc.append(f'{dean}')

    with doc.create(TextBlock(40, 85, 70)):
        doc.append('Докладная')

    with doc.create(TextBlock(180, 10, 80, indent=True)):
        doc.append(f'Довожу до Вашего сведения, что группа {group} не явилась на практические занятия с {start_time}-{end_time} {date} числа по дисциплине "{lesson_name}".')

    with doc.create(TextBlock(70, 10, 120)):
        doc.append(f'Преподаватель\n кафедры {department}')

    with doc.create(TextBlock(70, 135, 120)):
        doc.append(f'{name}')

    doc.generate_pdf('output/latex/dokladnoi', compiler='pdflatex', clean_tex=False)

def generateUmkFromLatex(token):
    umkDoc = Umk.query.filter_by(token=token).first()

    tex = open("latex/umk_scratch.tex", "r", encoding="utf-8")

    doc = Document(data=NoEscape(tex.read()), geometry_options={"left": "20mm", "right": "20mm", "top": "15mm", "bottom": "15mm"})
    doc.documentclass = Command(
        'documentclass',
        options=['11pt', 'a4paper'],
        arguments=['article'],
    )
    doc.packages.append(Package('geometry'))
    doc.packages.append(Package('titlesec'))
    doc.packages.append(Package('tabularx'))
    doc.packages.append(Package('ragged2e'))
    doc.packages.append(Package('inputenc', options=['utf8']))
    doc.packages.append(Package('babel', options=['english', 'russian']))
    doc.packages.append(Package('tempora'))
    doc.packages.append(Package('newtxmath'))

    doc.preamble.append(NoEscape(r'\newcommand{\HY}{\hyphenpenalty=25\exhyphenpenalty=25}'))
    doc.preamble.append(NoEscape(r'\newcolumntype{Z}{>{\HY\centering\arraybackslash\hspace{0pt}}X}'))
    doc.preamble.append(NoEscape(r'\newcolumntype{M}{>{\HY\RaggedRight\arraybackslash\hspace{0pt}}c}'))
    doc.preamble.append(NoEscape(r'\newcolumntype{L}{>{\HY\RaggedRight\arraybackslash\hspace{0pt}}l}'))

    doc.preamble.append(Command('date', NoEscape(r'')))
    doc.preamble.append(Command('titlelabel', NoEscape(r'\thetitle.\quad')))

    doc.preamble.append(NoEscape(r'\def\faculty{' + umkDoc.faculty + r'}'))
    doc.preamble.append(NoEscape(r'\def\department{' + umkDoc.department + r'}'))
    doc.preamble.append(NoEscape(r'\def\subject{' + umkDoc.subject + r'}'))
    doc.preamble.append(NoEscape(r'\def\group{' + umkDoc.group + r'}'))
    doc.preamble.append(NoEscape(r'\def\course{' + umkDoc.course + r'}'))
    doc.preamble.append(NoEscape(r'\def\studyTime{' + umkDoc.studyTime + r'}'))
    doc.preamble.append(NoEscape(r'\def\credits{' + umkDoc.credits + r'}'))

    ##########################################################################################

    themes = umkDoc.first_themes.split('; ')
    lections = umkDoc.first_lections.split('; ')
    seminars = umkDoc.first_seminars.split('; ')
    srsps = umkDoc.first_srsps.split('; ')
    srss = umkDoc.first_srss.split('; ')

    tableText = (r'\begin{center}'
                 r'\begin{tabularx}{ \textwidth }{|M|Z|Z|Z|Z|M|M|}'
                 r'\hline'
                 r'№ & \raggedright{Наименование темы} \\ \raggedleft{Объем часов} & Лекционные занятия & Семинарские/ Практические занятия &  СРОП & СРС \\'
                 r'\hline')

    for x in range(umkDoc.first_counts):
        tableText += (fr'{x + 1} & \raggedright {themes[x]} & {lections[x]} & {seminars[x]} & {srsps[x]} & {srss[x]} \\'
                      r'\hline')

    tableText += (r'\end{tabularx}'
                 r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\tematicsTable{' + tableText + r'}'))

    ##########################################################################################

    lecturers = umkDoc.second_lecturers.split('; ')
    lecturersText = ''
    for x in range(umkDoc.second_counts):
        lecturersText += fr'{lecturers[x]} \\' if (x != umkDoc.second_counts - 1) else fr'{lecturers[x]}'

    doc.preamble.append(NoEscape(r'\def\lecturers{' + lecturersText + r'}'))
    doc.preamble.append(NoEscape(r'\def\prerequisites{' + umkDoc.second_prerequisites + r'}'))
    doc.preamble.append(NoEscape(r'\def\postRequisites{' + umkDoc.second_post_requisites + r'}'))

    ##########################################################################################

    doc.preamble.append(NoEscape(r'\def\courseDescription{' + umkDoc.third_course_description + r'}'))

    ##########################################################################################

    loss = umkDoc.third_los.split('; ')
    methods = umkDoc.third_methods.split('; ')

    losAndMethodsText = (r'\begin{center}'
                 r'\begin{tabularx}{ \textwidth }'
                 r'{'
                 r'| >{\centering\arraybackslash}c'
                 r'| >{\centering\arraybackslash}X'
                 r'| >{\centering\arraybackslash}X |'
                 r'}'
                 r'\hline'
                 r'№ & Результаты обучения & Методы оценки достижимости результатов обучения \\'
                 r'\hline')

    for x in range(umkDoc.third_counts):
        losAndMethodsText += (fr'{x + 1} & {loss[x]} & {methods[x]} \\'
                      r'\hline')

    losAndMethodsText += (r'\end{tabularx}'
                  r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\losAndMethodsTable{' + losAndMethodsText + r'}'))

    ##########################################################################################

    doc.preamble.append(NoEscape(r'\def\teachingMethods{' + umkDoc.fourth_teaching_methods + r'}'))
    doc.preamble.append(NoEscape(r'\def\gradeMethods{' + umkDoc.fourth_grade_methods + r'}'))

    ##########################################################################################

    bls = umkDoc.fifth_bls.split('; ')
    als = umkDoc.fifth_als.split('; ')

    blAlText = (r'\begin{center}'
            r'\begin{tabularx}{ \textwidth }'
            r'{'
            r'| >{\centering\arraybackslash}c'
            r'| >{\centering\arraybackslash}X |'
            r'}'
            r'\hline'
            r'№ & Наименование учебников, пособий, используемых по курсу \\'
            r'\hline'
            r'\multicolumn{2}{|c|}{Основная литература} \\'
            r'\hline')

    for x in range(umkDoc.fifth_bl_counts):
        blAlText += (fr'{x + 1} & {bls[x]} \\'
                              r'\hline')

    blAlText += r' \multicolumn{2}{|c|}{Дополнительная литература} \\ \hline'

    for x in range(umkDoc.fifth_al_counts):
        blAlText += (fr'{x + 1} & {als[x]} \\'
                              r'\hline')

    blAlText += (r'\end{tabularx}'
                 r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\blAlText{' + blAlText + r'}'))

    ##########################################################################################

    lss = umkDoc.sixth_lss.split('; ')
    lps = umkDoc.sixth_lps.split('; ')

    lssLpsText = (r'\begin{center}'
                r'\begin{tabularx}{ \textwidth }'
                r'{'
                r'| >{\centering\arraybackslash}c'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X |'
                r'}'
                r'\hline'
                r'№ & Тема лекции & План лекции \\'
                r'\hline')

    for x in range(umkDoc.sixth_counts):
        lssLpsText += (fr'{x + 1} & {lss[x]} & {lps[x]} \\'
                 r'\hline')

    lssLpsText += (r'\end{tabularx}'
                 r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\lssLpsText{' + lssLpsText + r'}'))

    ##########################################################################################

    spss = umkDoc.seventh_spss.split('; ')
    spqs = umkDoc.seventh_spqs.split('; ')
    sprs = umkDoc.seventh_sprs.split('; ')
    spls = umkDoc.seventh_spls.split('; ')

    splpText = (r'\begin{center}'
                r'\begin{tabularx}{ \textwidth }'
                r'{'
                r'| >{\centering\arraybackslash}c'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X |'
                r'}'
                r'\hline'
                r'№ & Тема занятия & Вопросы и задания & Методические рекомендации (при необходимости) & Ссылка на перечень рекомендованных источников \\'
                r'\hline')

    for x in range(umkDoc.seventh_counts):
        splpText += (fr'{x + 1} & {spss[x]} & {spqs[x]} & {sprs[x]} & {spls[x]} \\'
                   r'\hline')

    splpText += (r'\end{tabularx}'
                   r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\splpText{' + splpText + r'}'))

    ##########################################################################################

    if umkDoc.eighth_counts is not None and umkDoc.eighth_counts > 0:
        slabs = umkDoc.eighth_slabs.split('; ')
        qlabs = umkDoc.eighth_qlabs.split('; ')
        rlabs = umkDoc.eighth_rlabs.split('; ')
        llabs = umkDoc.eighth_llabs.split('; ')

        labText = (r'\begin{center}'
                    r'\begin{tabularx}{ \textwidth }'
                    r'{'
                    r'| >{\centering\arraybackslash}c'
                    r'| >{\centering\arraybackslash}X'
                    r'| >{\centering\arraybackslash}X'
                    r'| >{\centering\arraybackslash}X'
                    r'| >{\centering\arraybackslash}X |'
                    r'}'
                    r'\hline'
                    r'№ & Тема занятия & Лабораторное задание & Методические рекомендации (при необходимости) & Ссылка на перечень рекомендованных источников \\'
                    r'\hline')

        for x in range(umkDoc.eighth_counts):
            labText += (fr'{x + 1} & {slabs[x]} & {qlabs[x]} & {rlabs[x]} & {llabs[x]} \\'
                         r'\hline')

        labText += (r'\end{tabularx}'
                     r'\end{center}')

        doc.preamble.append(NoEscape(r'\def\labText{' + labText + r'}'))
    else:
        doc.preamble.append(NoEscape(r'\def\labText{Учебным планом не предусмотрены}'))

    ##########################################################################################

    sropss = umkDoc.ninth_sropss.split('; ')
    sropqs = umkDoc.ninth_sropqs.split('; ')
    sroprs = umkDoc.ninth_sroprs.split('; ')
    sross = umkDoc.ninth_sross.split('; ')
    sroqs = umkDoc.ninth_sroqs.split('; ')
    srors = umkDoc.ninth_srors.split('; ')

    sropText = (r'\begin{center}'
                r'\begin{tabularx}{ \textwidth }'
                r'{'
                r'| >{\centering\arraybackslash}c'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X |'
                r'}'
                r'\hline'
                r'№ & Тема занятия & Задания & Методические рекомендации (при необходимости)\\'
                r'\hline')

    sroText = (r'\begin{center}'
                r'\begin{tabularx}{ \textwidth }'
                r'{'
                r'| >{\centering\arraybackslash}c'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X'
                r'| >{\centering\arraybackslash}X |'
                r'}'
                r'\hline'
                r'№ & Тема занятия & Задания & Методические рекомендации (при необходимости)\\'
                r'\hline')

    for x in range(umkDoc.ninth_srop_counts):
        sropText += (fr'{x + 1} & {sropss[x]} & {sropqs[x]} & {sroprs[x]} \\'
                     r'\hline')

    for x in range(umkDoc.ninth_sro_counts):
        sroText += (fr'{x + 1} & {sross[x]} & {sroqs[x]} & {srors[x]} \\'
                     r'\hline')

    sropText += (r'\end{tabularx}'
                 r'\end{center}')

    sroText += (r'\end{tabularx}'
                 r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\sropText{' + sropText + r'}'))
    doc.preamble.append(NoEscape(r'\def\sroText{' + sroText + r'}'))

    ##########################################################################################

    pws = umkDoc.tenth_pws.split('; ')
    pwsText = ''

    for x in range(umkDoc.tenth_counts):
        pwsText += fr'{x + 1}. {pws[x]} \\'

    doc.preamble.append(NoEscape(r'\def\pwsText{' + pwsText + r'}'))

    ##########################################################################################

    gps = umkDoc.eleventh_gps.split('; ')
    gpt = umkDoc.eleventh_gpt.split('; ')
    gpf = umkDoc.eleventh_gpf.split('; ')
    gpr = umkDoc.eleventh_gpr.split('; ')
    gpd = umkDoc.eleventh_gpd.split('; ')
    gpb = umkDoc.eleventh_gpb.split('; ')

    gpText = (r'\begin{center}'
            r'\begin{tabularx}{ \textwidth }'
            r'{'
            r'| >{\centering\arraybackslash}c'
            r'| >{\centering\arraybackslash}X'
            r'| >{\centering\arraybackslash}X'
            r'| >{\centering\arraybackslash}X'
            r'| >{\centering\arraybackslash}X'
            r'| >{\centering\arraybackslash}X'
            r'| >{\centering\arraybackslash}X |'
            r'}'
            r'\hline'
            r'№ & Тема занятия & Тип занятия & Вид задания & Форма отчета & Срок сдачи (неделя) & Баллы\\'
            r'\hline')

    for x in range(umkDoc.eleventh_counts):
        gpText += (fr'{x + 1} & {gps[x]} & {gpt[x]} & {gpf[x]} & {gpr[x]} & {gpd[x]} & {gpb[x]} \\'
                     r'\hline')

    gpText += (r'\end{tabularx}'
                 r'\end{center}')

    doc.preamble.append(NoEscape(r'\def\gpText{' + gpText + r'}'))

    ##########################################################################################

    acTexts = umkDoc.twelfth_texts.split('; ')

    doc.preamble.append(NoEscape(r'\def\acAText{' + acTexts[0] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acAMinusText{' + acTexts[1] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acBPlusText{' + acTexts[2] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acBText{' + acTexts[3] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acBMinusText{' + acTexts[4] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acCPlusText{' + acTexts[5] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acCText{' + acTexts[6] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acCMinusText{' + acTexts[7] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acDPlusText{' + acTexts[8] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acDText{' + acTexts[9] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acFxText{' + acTexts[10] + r'}'))
    doc.preamble.append(NoEscape(r'\def\acFText{' + acTexts[11] + r'}'))

    doc.generate_pdf('output/latex/umk', compiler='pdflatex', clean_tex=False)