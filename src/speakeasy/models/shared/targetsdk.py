"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from .interactiontype import InteractionType
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from speakeasy import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class TargetSDK:
    generate_gen_lock_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_gen_lock_id') }})
    r"""gen.lock ID (expected to be a uuid). The same as `id`. A unique identifier for the target."""
    generate_target: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_target') }})
    r"""eg `typescript`, `terraform`, `python`"""
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    r"""Unique identifier of the target the same as `generate_gen_lock_id`"""
    last_event_created_at: datetime = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_event_created_at'), 'encoder': utils.datetimeisoformat(False), 'decoder': dateutil.parser.isoparse }})
    r"""Timestamp when the event was created in the database."""
    last_event_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_event_id') }})
    r"""Unique identifier of the last event for the target"""
    last_event_interaction_type: InteractionType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('last_event_interaction_type') }})
    r"""Type of interaction."""
    commit_head: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('commit_head'), 'exclude': lambda f: f is None }})
    r"""Remote commit ID."""
    continuous_integration_environment: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('continuous_integration_environment'), 'exclude': lambda f: f is None }})
    r"""Name of the CI environment."""
    generate_config_post_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_config_post_version'), 'exclude': lambda f: f is None }})
    r"""Version of the generated target (post generation)"""
    generate_gen_lock_pre_features: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_gen_lock_pre_features'), 'exclude': lambda f: f is None }})
    r"""Features prior to generation"""
    generate_gen_lock_pre_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_gen_lock_pre_version'), 'exclude': lambda f: f is None }})
    r"""Artifact version for the Previous Generation"""
    generate_published: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_published'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the target was considered published."""
    generate_target_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_target_name'), 'exclude': lambda f: f is None }})
    r"""The name of the target as defined by the user."""
    generate_target_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generate_target_version'), 'exclude': lambda f: f is None }})
    r"""The version of the Speakeasy generator for this target eg v2 of the typescript generator."""
    gh_action_organization: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gh_action_organization'), 'exclude': lambda f: f is None }})
    r"""GitHub organization of the action."""
    gh_action_repository: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gh_action_repository'), 'exclude': lambda f: f is None }})
    r"""GitHub repository of the action."""
    gh_action_run_link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gh_action_run_link'), 'exclude': lambda f: f is None }})
    r"""Link to the GitHub action run."""
    gh_action_version: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gh_action_version'), 'exclude': lambda f: f is None }})
    r"""Version of the GitHub action."""
    git_relative_cwd: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_relative_cwd'), 'exclude': lambda f: f is None }})
    r"""Current working directory relative to the git root."""
    git_remote_default_owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_remote_default_owner'), 'exclude': lambda f: f is None }})
    r"""Default owner for git remote."""
    git_remote_default_repo: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_remote_default_repo'), 'exclude': lambda f: f is None }})
    r"""Default repository name for git remote."""
    git_user_email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_user_email'), 'exclude': lambda f: f is None }})
    r"""User email from git configuration."""
    git_user_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('git_user_name'), 'exclude': lambda f: f is None }})
    r"""User's name from git configuration. (not GitHub username)"""
    hostname: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hostname'), 'exclude': lambda f: f is None }})
    r"""Remote hostname."""
    repo_label: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('repo_label'), 'exclude': lambda f: f is None }})
    r"""Label of the git repository."""
    success: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('success'), 'exclude': lambda f: f is None }})
    r"""Indicates whether the event was successful."""
    

