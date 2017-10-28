from tastypie.resources import ModelResource, ALL
from app.models import Projects


class ProjectResource(ModelResource):
    class Meta:
        queryset = Projects.objects.all()
        resource_name = 'project'
        filtering = {
                "project_name": ALL,
            }
