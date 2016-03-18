from src.business.configuration.configProject import ConfigProject
from src.business.configuration.configSystem import ConfigSystem as cs

p = cs()

print(str(p.project_path()))
# print(p.get_site_settings())
s = ConfigProject(p.project_path())
# s.setup_settings("test.ini")

# s.set_site_settings(False, True, "ab", "cd")
# s.save_settings()
# s.setup_settings()
print(s.get_site_settings())
print(s.get_geographic_settings())