from flask import request, send_file, jsonify
from init import create_app
from extensions import db
from umk import createUmk, updateUmkIndex, updateUmkFirst, updateUmkSecond, updateUmkThird, updateUmkFourth, updateUmkFifth, updateUmkSixth, updateUmkSeventh, updateUmkEighth, updateUmkNinth, updateUmkTenth, updateUmkEleventh, updateUmkTwelfth
from generate_from_word import generateUmkFromWord, generateDokladnoiFromWord

app = create_app()

@app.route("/")
def dokladnoi():
    input_name = request.args.get('name', '')
    input_date = request.args.get('date', '')
    input_faculty = request.args.get('faculty', '')
    input_dean = request.args.get('dean', '')
    input_department = request.args.get('department', '')
    input_group = request.args.get('group', '')
    input_lesson_name = request.args.get('lesson_name', '')
    input_lesson_type = request.args.get('lesson_type', '')
    input_start_time = request.args.get('start_time', '')
    input_end_time = request.args.get('end_time', '')

    generateDokladnoiFromWord(input_name, input_date, input_faculty, input_dean, input_department, input_group, input_lesson_name, input_lesson_type, input_start_time, input_end_time)

    return send_file('output/word/dokladnoi.pdf')

@app.route("/umk", methods = ['POST'])
def umk():
    input_language = request.form.get('language', '')

    token = createUmk(input_language)

    return token

@app.route("/umk-index", methods = ['POST'])
def umk_index():
    token = request.headers.get('Umk-token')
    input_faculty = request.form.get('faculty', '')
    input_department = request.form.get('department', '')
    input_subject = request.form.get('subject', '')
    input_group = request.form.get('group', '')
    input_course = request.form.get('course', '')
    input_study_time = request.form.get('study_time', '')
    input_credits = request.form.get('credits', '')

    updateUmkIndex(token, input_faculty, input_department, input_subject, input_group, input_course, input_study_time, input_credits)

    return jsonify(success=True)

@app.route("/umk/first", methods = ['POST'])
def umk_first():
    token = request.headers.get('Umk-token')
    input_counts = request.form.get('counts', '')
    input_themes = request.form.get('themes', '')
    input_lections = request.form.get('lections', '')
    input_seminars = request.form.get('seminars', '')
    input_labs = request.form.get('labs', '')
    input_srsps = request.form.get('srsps', '')
    input_srss = request.form.get('srss', '')

    updateUmkFirst(token, input_counts, input_themes, input_lections, input_seminars, input_labs, input_srsps, input_srss)

    return jsonify(success=True)

@app.route("/umk/second", methods = ['POST'])
def umk_second():
    token = request.headers.get('Umk-token')
    input_counts = request.form.get('counts', '')
    input_lecturers = request.form.get('lecturers', '')
    input_prerequisites = request.form.get('prerequisites', '')
    input_post_requisites = request.form.get('postRequisites', '')

    updateUmkSecond(token, input_counts, input_lecturers, input_prerequisites, input_post_requisites)

    return jsonify(success=True)

@app.route("/umk/third", methods = ['POST'])
def umk_third():
    token = request.headers.get('Umk-token')
    input_counts = request.form.get('counts', '')
    input_los = request.form.get('los', '')
    input_methods = request.form.get('methods', '')
    input_course_description = request.form.get('courseDescription', '')

    updateUmkThird(token, input_counts, input_los, input_methods, input_course_description)

    return jsonify(success=True)

@app.route("/umk/fourth", methods = ['POST'])
def umk_fourth():
    token = request.headers.get('Umk-token')

    input_teaching_methods = request.form.get('teachingMethods', '')
    input_grade_methods = request.form.get('gradeMethods', '')

    updateUmkFourth(token, input_teaching_methods, input_grade_methods)

    return jsonify(success=True)

@app.route("/umk/fifth", methods = ['POST'])
def umk_fifth():
    token = request.headers.get('Umk-token')

    input_bl_counts = request.form.get('blCounts', '')
    input_al_counts = request.form.get('alCounts', '')
    input_bls = request.form.get('bls', '')
    input_als = request.form.get('als', '')

    updateUmkFifth(token, input_bl_counts, input_al_counts, input_bls, input_als)

    return jsonify(success=True)

@app.route("/umk/sixth", methods = ['POST'])
def umk_sixth():
    token = request.headers.get('Umk-token')

    input_counts = request.form.get('counts', '')
    input_lss = request.form.get('lss', '')
    input_lps = request.form.get('lps', '')

    updateUmkSixth(token, input_counts, input_lss, input_lps)

    return jsonify(success=True)

@app.route("/umk/seventh", methods = ['POST'])
def umk_seventh():
    token = request.headers.get('Umk-token')

    input_counts = request.form.get('counts', '')
    input_spss = request.form.get('spss', '')
    input_spqs = request.form.get('spqs', '')
    input_sprs = request.form.get('sprs', '')
    input_spls = request.form.get('spls', '')

    updateUmkSeventh(token, input_counts, input_spss, input_spqs, input_sprs, input_spls)

    return jsonify(success=True)

@app.route("/umk/eighth", methods = ['POST'])
def umk_eighth():
    token = request.headers.get('Umk-token')

    input_counts = request.form.get('counts', '')
    input_slabs = request.form.get('slabs', '')
    input_qlabs = request.form.get('qlabs', '')
    input_rlabs = request.form.get('rlabs', '')
    input_llabs = request.form.get('llabs', '')

    updateUmkEighth(token, input_counts, input_slabs, input_qlabs, input_rlabs, input_llabs)

    return jsonify(success=True)

@app.route("/umk/ninth", methods = ['POST'])
def umk_ninth():
    token = request.headers.get('Umk-token')

    input_srop_counts = request.form.get('sropCounts', '')
    input_sro_counts = request.form.get('sroCounts', '')
    input_sropss = request.form.get('sropss', '')
    input_sropqs = request.form.get('sropqs', '')
    input_sroprs = request.form.get('sroprs', '')
    input_sross = request.form.get('sross', '')
    input_sroqs = request.form.get('sroqs', '')
    input_srors = request.form.get('srors', '')

    updateUmkNinth(token, input_srop_counts, input_sro_counts, input_sropss, input_sropqs, input_sroprs, input_sross, input_sroqs, input_srors)

    return jsonify(success=True)

@app.route("/umk/tenth", methods = ['POST'])
def umk_tenth():
    token = request.headers.get('Umk-token')

    input_counts = request.form.get('counts', '')
    input_pws = request.form.get('pws', '')

    updateUmkTenth(token, input_counts, input_pws)

    return jsonify(success=True)

@app.route("/umk/eleventh", methods = ['POST'])
def umk_eleventh():
    token = request.headers.get('Umk-token')

    input_counts = request.form.get('counts', '')
    input_gps = request.form.get('gps', '')
    input_gpt = request.form.get('gpt', '')
    input_gpf = request.form.get('gpf', '')
    input_gpr = request.form.get('gpr', '')
    input_gpd = request.form.get('gpd', '')
    input_gpb = request.form.get('gpb', '')

    updateUmkEleventh(token, input_counts, input_gps, input_gpt, input_gpf, input_gpr, input_gpd, input_gpb)

    return jsonify(success=True)

@app.route("/umk/twelfth", methods = ['POST'])
def umk_twelfth():
    token = request.headers.get('Umk-token')

    input_texts = request.form.get('texts', '')

    updateUmkTwelfth(token, input_texts)

    generateUmkFromWord(token)

    return send_file('output/word/umk.pdf')

@app.route("/umk/docx", methods = ['POST'])
def umk_docx():
    token = request.headers.get('Umk-token')

    return generateUmkFromWord(token)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(host="0.0.0.0", port=8000, debug=True)