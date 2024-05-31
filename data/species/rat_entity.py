from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus
import constants.species
import constants.abilities


SPECIES_ENTITY_RAT = SpeciesEntity(
    key=constants.species.Species.RAT,
    description=(
        'Крысы самые многочисленные невелички в мире и занимают  восточные земли Государством Клеоссия '
        'и признанная только Котовьей Империей Клетоссией. <ins>Обладают живым умом и гибким телом</ins>. '
        'Многие из них прослыли в мире, как плуты и <ins>относятся к ним подозрительно</ins> из-за этого и из-за '
        'их многочисленности и привычки мигрировать в другие государства.  Верят они либо в их '
        'бессмертного (наверное) императора, либо в силу духов предков.'
    ),
    size_description=(
        'Вы соразмерны кротам по своим размерам, а кроме этого и уже их в плечах около **45-50 сантиметров**.<br>'
        '**Размер: <ins>Средний</ins>**'
    ),
    speed_in_meters=20,
    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Клеосском**.',
    additional_features=[
        'Увертливость',
        'Зрение в темноте',
    ],
    image_path='./images/rat.png',
    species_abilities_bonuses=[
        SpeciesAbilitiesBonus(
            abilities_bonuses=[
                SpeciesAbilityBonus(key=constants.abilities.Ability.DEXTERITY, bonus=2),
                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=1),
            ],
        ),
    ]
)
