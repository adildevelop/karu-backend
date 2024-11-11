from uuid import uuid4
from extensions import db

class Umk(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128), unique=True, nullable=False)
    language = db.Column(db.String(10), nullable=False)
    faculty = db.Column(db.String(255), nullable=True)
    department = db.Column(db.String(255), nullable=True)
    subject = db.Column(db.String(255), nullable=True)
    group = db.Column(db.String(255), nullable=True)
    course = db.Column(db.String(255), nullable=True)
    studyTime = db.Column(db.String(255), nullable=True)
    credits = db.Column(db.String(255), nullable=True)
    first_counts = db.Column(db.Integer, nullable=True)
    first_themes = db.Column(db.Text, nullable=True)
    first_lections = db.Column(db.String(255), nullable=True)
    first_seminars = db.Column(db.String(255), nullable=True)
    first_labs = db.Column(db.String(255), nullable=True)
    first_srsps = db.Column(db.String(255), nullable=True)
    first_srss = db.Column(db.String(255), nullable=True)
    second_counts = db.Column(db.Integer, nullable=True)
    second_lecturers = db.Column(db.Text, nullable=True)
    second_prerequisites = db.Column(db.Text, nullable=True)
    second_post_requisites = db.Column(db.Text, nullable=True)
    third_counts = db.Column(db.Integer, nullable=True)
    third_los = db.Column(db.Text, nullable=True)
    third_methods = db.Column(db.Text, nullable=True)
    third_course_description = db.Column(db.Text, nullable=True)
    fourth_teaching_methods = db.Column(db.Text, nullable=True)
    fourth_grade_methods = db.Column(db.Text, nullable=True)
    fifth_bl_counts = db.Column(db.Integer, nullable=True)
    fifth_al_counts = db.Column(db.Integer, nullable=True)
    fifth_bls = db.Column(db.Text, nullable=True)
    fifth_als = db.Column(db.Text, nullable=True)
    sixth_counts = db.Column(db.Integer, nullable=True)
    sixth_lss = db.Column(db.Text, nullable=True)
    sixth_lps = db.Column(db.Text, nullable=True)
    seventh_counts = db.Column(db.Integer, nullable=True)
    seventh_spss = db.Column(db.Text, nullable=True)
    seventh_spqs = db.Column(db.Text, nullable=True)
    seventh_sprs = db.Column(db.Text, nullable=True)
    seventh_spls = db.Column(db.Text, nullable=True)
    eighth_counts = db.Column(db.Integer, nullable=True)
    eighth_slabs = db.Column(db.Text, nullable=True)
    eighth_qlabs = db.Column(db.Text, nullable=True)
    eighth_rlabs = db.Column(db.Text, nullable=True)
    eighth_llabs = db.Column(db.Text, nullable=True)
    ninth_srop_counts = db.Column(db.Integer, nullable=True)
    ninth_sro_counts = db.Column(db.Integer, nullable=True)
    ninth_sropss = db.Column(db.Text, nullable=True)
    ninth_sropqs = db.Column(db.Text, nullable=True)
    ninth_sroprs = db.Column(db.Text, nullable=True)
    ninth_sross = db.Column(db.Text, nullable=True)
    ninth_sroqs = db.Column(db.Text, nullable=True)
    ninth_srors = db.Column(db.Text, nullable=True)
    tenth_counts = db.Column(db.Integer, nullable=True)
    tenth_pws = db.Column(db.Text, nullable=True)
    eleventh_counts = db.Column(db.Integer, nullable=True)
    eleventh_gps = db.Column(db.Text, nullable=True)
    eleventh_gpt = db.Column(db.Text, nullable=True)
    eleventh_gpf = db.Column(db.Text, nullable=True)
    eleventh_gpr = db.Column(db.Text, nullable=True)
    eleventh_gpd = db.Column(db.Text, nullable=True)
    eleventh_gpb = db.Column(db.Text, nullable=True)
    twelfth_texts = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return self.id

def createUmk(language):
    rand_token = uuid4().hex

    umk = Umk(
        token = rand_token,
        language = language,
    )

    db.session.add(umk)
    db.session.commit()

    return rand_token

def updateUmkIndex(token, faculty, department, subject, group, course, study_time, credits):
    umk = Umk.query.filter_by(token=token).first()
    umk.faculty = faculty
    umk.department = department
    umk.subject = subject
    umk.group = group
    umk.course = course
    umk.studyTime = study_time
    umk.credits = credits

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkFirst(token, counts, themes, lections, seminars, labs, srsps, srss):
    umk = Umk.query.filter_by(token=token).first()
    umk.first_counts = int(counts)
    umk.first_themes = themes
    umk.first_lections = lections
    umk.first_seminars = seminars
    umk.first_labs = labs
    umk.first_srsps = srsps
    umk.first_srss = srss

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkSecond(token, counts, lecturers, prerequisites, postRequisites):
    umk = Umk.query.filter_by(token=token).first()
    umk.second_counts = int(counts)
    umk.second_lecturers = lecturers
    umk.second_prerequisites = prerequisites
    umk.second_post_requisites = postRequisites

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkThird(token, counts, los, methods, course_description):
    umk = Umk.query.filter_by(token=token).first()
    umk.third_counts = int(counts)
    umk.third_los = los
    umk.third_methods = methods
    umk.third_course_description = course_description

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkFourth(token, teaching_methods, grade_methods):
    umk = Umk.query.filter_by(token=token).first()
    umk.fourth_teaching_methods = teaching_methods
    umk.fourth_grade_methods = grade_methods

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkFifth(token, bl_counts, al_counts, bls, als):
    umk = Umk.query.filter_by(token=token).first()
    umk.fifth_bl_counts = int(bl_counts)
    umk.fifth_al_counts = int(al_counts)
    umk.fifth_bls = bls
    umk.fifth_als = als

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkSixth(token, counts, lss, lps):
    umk = Umk.query.filter_by(token=token).first()
    umk.sixth_counts = int(counts)
    umk.sixth_lss = lss
    umk.sixth_lps = lps

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkSeventh(token, counts, spss, spqs, sprs, spls):
    umk = Umk.query.filter_by(token=token).first()
    umk.seventh_counts = int(counts)
    umk.seventh_spss = spss
    umk.seventh_spqs = spqs
    umk.seventh_sprs = sprs
    umk.seventh_spls = spls

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkEighth(token, counts, slabs, qlabs, rlabs, llabs):
    umk = Umk.query.filter_by(token=token).first()
    umk.eighth_counts = int(counts)
    umk.eighth_slabs = slabs
    umk.eighth_qlabs = qlabs
    umk.eighth_rlabs = rlabs
    umk.eighth_llabs = llabs

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkNinth(token, srop_counts, sro_counts, sropss, sropqs, sroprs, sross, sroqs, srors):
    umk = Umk.query.filter_by(token=token).first()
    umk.ninth_srop_counts = int(srop_counts)
    umk.ninth_sro_counts = int(sro_counts)
    umk.ninth_sropss = sropss
    umk.ninth_sropqs = sropqs
    umk.ninth_sroprs = sroprs
    umk.ninth_sross = sross
    umk.ninth_sroqs = sroqs
    umk.ninth_srors = srors

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkTenth(token, counts, pws):
    umk = Umk.query.filter_by(token=token).first()
    umk.tenth_counts = int(counts)
    umk.tenth_pws = pws

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkEleventh(token, counts, gps, gpt, gpf, gpr, gpd, gpb):
    umk = Umk.query.filter_by(token=token).first()
    umk.eleventh_counts = int(counts)
    umk.eleventh_gps = gps
    umk.eleventh_gpt = gpt
    umk.eleventh_gpf = gpf
    umk.eleventh_gpr = gpr
    umk.eleventh_gpd = gpd
    umk.eleventh_gpb = gpb

    db.session.add(umk)
    db.session.commit()

    return True

def updateUmkTwelfth(token, texts):
    umk = Umk.query.filter_by(token=token).first()
    umk.twelfth_texts = texts

    db.session.add(umk)
    db.session.commit()

    return True