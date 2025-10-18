import asyncio
import json
from urllib.parse import urlparse
from datetime import datetime,  timezone
from math import ceil
from flask import Blueprint, Response, jsonify, redirect, request, render_template, flash, url_for
from flask_login import current_user, login_required
from app.account.account_core import add_favorite, remove_favorite
from app.import_github_project.cron_check_updates import disable_schedule_job, enable_schedule_job, modify_schedule_job, remove_schedule_job
from app.import_github_project.update_github_project import Check_for_rule_updates
from app.misp.misp_core import content_convert_to_misp_object
from app.rule_type.main_format import  extract_rule_from_repo, process_and_import_fixed_rule, verify_syntax_rule_by_format
from app.import_github_project.untils_import import clone_or_access_repo, delete_existing_repo_folder, fill_all_void_field, get_licst_license, git_pull_repo, github_repo_metadata, valider_repo_github

rule_blueprint = Blueprint(
    'rule',
    __name__,
    template_folder='templates',    
    static_folder='static'
)

@rule_blueprint.route("/ws", methods=['GET'])
def rules_list() -> jsonify:       
    return {"message": "Hello there"}
