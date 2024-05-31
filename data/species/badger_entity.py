from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_BADGER = SpeciesEntity(
    key=constants.species.Species.BADGER,
    description=(
        'Барсуки самые крупные и сильные из невеличек, но своего государства им создать не удалось. '
        'Они обычно <ins>живут либо поодиночке</ins> в разных городах и селах, <ins>либо маленькими отдельными коммунами</ins> '
        'которым разрешают жить на территориях государств <ins>за счет обеспечения</ins> близ лежащих территорий <ins>защитой</ins>. '
        'Зачастую живут в необжитых землях и лесах, молятся силам природы и не отказываются от наследия Лет Крови.'
    ),
    size_description=(
        'Самые крупные из невеличек, рост в среднем составляет **85-90 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=15,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на языке страны, в которой проживаете.',
    additional_features=[
        'Выживаемость',
        'Угрожающий вид',
    ],
    image_path='./images/badger.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.STRENGTH, bonus=2),
                SpeciesAbilityBonus(key=constants.abilities.Ability.CONSTITUTION, bonus=1),
            ],
        ),
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.STRENGTH, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.CONSTITUTION, bonus=2),
            ],
        ),
    ]
)
