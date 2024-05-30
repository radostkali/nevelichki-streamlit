import constants.abilities
import constants.species
from entities import SpeciesEntity, SpeciesAbilitiesBonus, SpeciesAbilityBonus


class SpeciesDAO:

    def get_species(self, species: constants.species.Species) -> SpeciesEntity:
        match species:
            case constants.species.Species.MOLE:
                return SpeciesEntity(
                    key=species,
                    description=(
                        'Кроты занимают важное место в экономике мира невеличек благодаря многочисленным филиалам банка Кротье '
                        'в котором храняться многие деньги многих государств, кроме Империи Котовия. Кроты <ins>отличаются крепким '
                        'телосложением</ins>, <ins>физической силой</ins> и развитым, за счет отличный системы образования Королевства Нор, '
                        '<ins>интеллектом</ins>. К ним относятся уважительно и нейтрально. <ins>В большинстве своем являются атеистами</ins> '
                        'или последователями Скачка.'
                    ),
                    size_description=(
                        'Вы ниже большинства других невеличек, но шире в плечах и крепче, средний рост около **45-50 сантиметров**.<br>'
                        '**Размер: <ins>Средний</ins>**'
                    ),
                    speed_in_meters=15,
                    languages_description='Вы можете говорить, читать и писать на **Общем** и на **Норском**.',
                    additional_features=[
                        'Чувство направления под землей',
                        'Зрение в темноте',
                    ],
                    image_path='./images/mole.png',
                    species_abilities_bonuses=[
                        SpeciesAbilitiesBonus(
                            abilities_bonuses=[
                                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=2),
                                SpeciesAbilityBonus(key=constants.abilities.Ability.STRENGTH, bonus=1),
                            ],
                        ),
                        SpeciesAbilitiesBonus(
                            abilities_bonuses=[
                                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=1),
                                SpeciesAbilityBonus(key=constants.abilities.Ability.STRENGTH, bonus=2),
                            ],
                        ),
                        SpeciesAbilitiesBonus(
                            abilities_bonuses=[
                                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=2),
                                SpeciesAbilityBonus(key=constants.abilities.Ability.CONSTITUTION, bonus=1),
                            ],
                        ),
                        SpeciesAbilitiesBonus(
                            abilities_bonuses=[
                                SpeciesAbilityBonus(key=constants.abilities.Ability.INTELLIGENCE, bonus=1),
                                SpeciesAbilityBonus(key=constants.abilities.Ability.CONSTITUTION, bonus=2),
                            ],
                        ),
                    ]
                )
