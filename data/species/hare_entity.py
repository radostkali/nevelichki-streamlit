from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_HARE = SpeciesEntity(
    key=constants.species.Species.HARE,
    description=(
        'Зайцы, как нация известна как главные инноваторы , как технологические так и магические, хотя изначально, '
        'способности отдельно взятых зайцев направлены в первую очередь на <ins>хаотичную научную деятельность вследствии '
        'природного любопытство</ins>. Практически все зайцы за редким исключением <ins>верят в Скачек</ins>, что не '
        'удивительно, ведь в их стране эта религия и зародилась.'
    ),
    size_description=(
        'Вы довольно высоки относительно дригих невеличек, но зачастую худы около **70-75 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=20,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Крайнем**.',
    additional_features=[
        'Резкий прыжок',
        'Зрение в темноте',
    ],
    image_path='./images/hare.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=2),
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=1),
            ],
        ),
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=2),
            ],
        ),
    ]
)
