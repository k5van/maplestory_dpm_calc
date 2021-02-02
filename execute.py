# from dpmModule.util.dpmgenerator import IndividualDPMGenerator

# job_name = '제로'
# gen = IndividualDPMGenerator(job_name)
# print(job_name, gen.get_dpm(spec_name="8000", ulevel=8000))


# import dpmModule.jobs.nightlord as nightlord
# from dpmModule.character.characterTemplate import TemplateGenerator

# character = TemplateGenerator('8500').get_template(8500)
# gen = nightlord.JobGenerator()
# v_builder = core.NJBStyleVBuilder(skill_core_level=25, each_enhanced_amount=17)
# graph = gen.package(character, v_builder)

#자세한 사용 방법은 dpmModule의 readme를 참조하십시오.



import dpmModule
from dpmModule.util.dpmgenerator import IndividualDPMGenerator
import dpmModule.character.characterTemplateHigh as template
gen = IndividualDPMGenerator('나이트로드', template.getU6000CharacterTemplate)
print(gen.get_dpm(ulevel = 6000))