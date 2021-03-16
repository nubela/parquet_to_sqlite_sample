import os
import uuid
from pprint import pprint
import pandas as pd
import manager
import pyarrow.parquet as pq

from model import Course, Education, Experience, HonourAward, Language, Organization, Patent, Profile, Project, Publication, TestScore, VolunteeringExperience, session

manager = manager.Manager()


@manager.command
def get_parquet_file_paths():
    files = os.listdir()
    return list(filter(lambda x: x.startswith('profile'), files))


@manager.command
def import_profiles():
    for file_path in filter(lambda x: x.startswith('profile-'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(idx)
            p = Profile()
            p.id = row['id']
            p.created = row['created']
            p.updated = row['updated']
            p.city = row['city']
            p.first_name = row['first_name']
            p.last_name = row['last_name']
            p.headline = row['headline']
            p.state = row['state']
            p.summary = row['summary']
            session.add(p)
        session.commit()


@manager.command
def import_courses():
    for file_path in filter(lambda x: x.startswith('profile_course'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"course {idx}")
            c = Course()
            c.id = uuid.uuid4().hex
            c.name = row['name']
            c.number = row['number']
            c.profile_id = row['profile_id']
            session.add(c)
        session.commit()


@manager.command
def import_education():
    for file_path in filter(lambda x: x.startswith('profile_education'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"education {idx}")
            c = Education()
            c.id = str(uuid.uuid4())
            c.created = row['created']
            c.updated = row['updated']
            c.starts_at = row['starts_at'] if not pd.isnull(row['starts_at']) else None
            c.ends_at = row['ends_at'] if not pd.isnull(row['ends_at']) else None
            c.field_of_study = row['field_of_study']
            c.degree_name = row['degree_name']
            c.school = row['school']
            c.school_profile_url = row['school_profile_url']
            c.profile_id = row['profile_id']
            session.add(c)
        session.commit()


@manager.command
def import_experiences():
    for file_path in filter(lambda x: x.startswith('profile_experience'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"exp {idx}")
            c = Experience()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.starts_at = row['starts_at']  if not pd.isnull(row['starts_at']) else None
            c.ends_at = row['ends_at'] if not pd.isnull(row['ends_at']) else None
            c.profile_id = row['profile_id']
            c.company = row['company']
            c.company_profile_url = row['company_profile_url']
            c.title = row['title']
            c.location = row['location']
            c.description = row['description']
            session.add(c)
        session.commit()


@manager.command
def import_honour_awards():
    for file_path in filter(lambda x: x.startswith('profile_honour_award'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"honour award {idx}")
            c = HonourAward()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.title = row['title']
            c.issuer = row['issuer']
            c.issued_on = row['issued_on'] if not pd.isnull(row['issued_on']) else None
            c.description = row['description']
            session.add(c)
        session.commit()


@manager.command
def import_languages():
    for file_path in filter(lambda x: x.startswith('profile_language'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"lang {idx}")
            c = Language()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.name = row['name']
            c.profile_id = row['profile_id']
            session.add(c)
        session.commit()


@manager.command
def import_orgs():
    for file_path in filter(lambda x: x.startswith('profile_organization'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"org {idx}")
            c = Organization()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.starts_at = row['starts_at'] if not pd.isnull(row['starts_at']) else None
            c.ends_at = row['ends_at'] if not pd.isnull(row['ends_at']) else None
            c.name = row['name']
            c.title = row['title']
            c.description = row['description']
            session.add(c)
        session.commit()


@manager.command
def import_patents():
    for file_path in filter(lambda x: x.startswith('profile_patent'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"patent {idx}")
            c = Patent()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.title = row['title']
            c.description = row['description']
            c.url = row['url']
            c.issued_on = row['issued_on'] if not pd.isnull(row['issued_on']) else None
            c.issuer = row['issuer']
            c.patent_number = row['patent_number']

            session.add(c)
        session.commit()


@manager.command
def import_project():
    for file_path in filter(lambda x: x.startswith('profile_project'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"project {idx}")
            c = Project()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.title = row['title']
            c.description = row['description']
            c.url = row['url']
            session.add(c)
        session.commit()


@manager.command
def import_publications():
    for file_path in filter(lambda x: x.startswith('profile_publication'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"publication {idx}")
            c = Publication()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.name = row['name']
            c.publisher = row['publisher']
            c.published_on = row['published_on'] if not pd.isnull(row['published_on']) else None
            c.description = row['description']
            c.url = row['url']
            session.add(c)
        session.commit()


@manager.command
def import_test_scores():
    for file_path in filter(lambda x: x.startswith('profile_test_score'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"test score {idx}")
            c = TestScore()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.name = row['name']
            c.score = row['score']
            c.date_on = row['date_on'] = row['date_on'] if not pd.isnull(row['date_on']) else None
            c.description = row['description']
            session.add(c)
        session.commit()


@manager.command
def import_volunteering():
    for file_path in filter(lambda x: x.startswith('profile_volunteering_experience'), get_parquet_file_paths()):
        table = pq.read_table(file_path)
        df = table.to_pandas()
        for idx, row in df.iterrows():
            print(f"vol {idx}")
            c = VolunteeringExperience()
            c.id = uuid.uuid4().hex
            c.created = row['created']
            c.updated = row['updated']
            c.profile_id = row['profile_id']
            c.starts_at = row['starts_at'] if not pd.isnull(row['starts_at']) else None
            c.ends_at = row['ends_at'] if not pd.isnull(row['ends_at']) else None
            c.cause = row['cause']
            c.company = row['company']
            c.company_profile_url = row['company_profile_url']
            c.location = row['location']
            c.title = row['title']
            session.add(c)
        session.commit()


@manager.command
def test():
    fp = 'profile_volunteering_experience-0.parquet'
    table = pq.read_table(fp)
    df = table.to_pandas()
    for index, row in df.iterrows():
        print(row)
        return


if __name__ == '__main__':
    manager.main()
