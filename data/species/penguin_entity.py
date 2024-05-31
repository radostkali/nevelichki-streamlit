from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_PENGUIN = SpeciesEntity(
    key=constants.species.Species.PENGUIN,
    description=(
        'Пингвины, как и песцы имеют свое северное государство и в основном занимаются борьбой с природой, '
        'и многочисленными хищниками арктической пустыни. Как и песцы, а так же коты, <ins>пренебрегают некоторыми '
        'общими принятыми запретами</ins>, например о поедании рыбы. Верят так же в Рахака, или как аристократия '
        'Империи в Скачек.'
    ),
    size_description=(
        'Рост пингвинов живущих на севере в среднем составляет **55-60 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=15,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Пенгунианском**.',
    additional_features=[
        'Быстрое плавание',
        'Устойчивость к холоду',
    ],
    image_path='./images/penguin.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.WISDOM, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.CONSTITUTION, bonus=1),
            ],
        ),
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.WISDOM, bonus=1),
                SpeciesAbilityBonus(key=constants.abilities.Ability.STRENGTH, bonus=1),
            ],
        ),
    ]
)
