from src.business.configuration.configProject import ConfigProject

s = ConfigProject("test")
# s.setup_settings("test")

# s.set_site_settings(False, True, "ab", "cd")
# s.save_settings()
# s.setup_settings()
print(s.get_site_settings())